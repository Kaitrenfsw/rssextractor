from bs4 import BeautifulSoup
from pprint import pprint
from datetime import datetime
from urllib.request import urlopen as uReq
from urllib import request as urllibrequest
import request
import feedparser
import json
import urllib3
import pika
import os

# connect to RabbitMQ

connected = False

while(not connected):
	try:
		connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq-docker'))
		connected = True
	except:
		pass

channel = connection.channel()

channel.queue_declare(queue='preprocessing_queue')

# base url and data from this source
source_name = "DZone"
source_id = 24
rss_url= "http://feeds.dzone.com/security"
date_format = '%a, %d %b %Y %X'
default_image = "https://dzone.com/themes/dz20/images/DZLogo.png"
first_exec = False

# check if file exist and set 'first_exec' var

dir_path = "feed_logs/"
file_name = "dzone_security_feed_log.txt"

if os.path.exists(dir_path+file_name):
	file_mode = 'r'
	first_exec = False
	print("Archivo existe")
	print("Mode: "+file_mode)
else:
	file_mode = 'w+'
	first_exec = True
	last_record = "first_exec"
	print("Archivo no existe.")
	print("Mode: "+file_mode)

	with open(dir_path+file_name, file_mode) as f:
		print("Log file created...")
		f.write("First Execution")

# parse feed
	# if first execution add here special behavior, such as getting historical data
d = feedparser.parse(rss_url)

# list of rss entries
entries = d['entries']

# check last recorded entry if file already existed

if not first_exec:
	with open(dir_path+file_name, file_mode) as f:
		last_record = f.readline()
		file_mode = 'w+'

# create empty publication list

documents = {"documents": [ ]}

# get data from non-recorded entries and original links to publications

first_loop = True

for entry in entries:

	# stop loop if entry is already recorded
	
	title = entry['title']
	if last_record == title:
		print("This entry was already obtained.")
		print("Stopping script.")
		break

	# save first entry as new last record
	if first_loop:
		with open(dir_path+file_name, file_mode) as f:
			f.write(title)
		first_loop = False

	# scrap html embeded summary

	summary = entry['summary']
	summary_soup = BeautifulSoup(summary, 'html.parser')

	# empty dictionary to save entry data
	
	document = {}

	# save base data (title, p_date, url, image, source_id, source_name, summary[if-any])

	document['title'] = title
	original_link = entry['link']
	document['url'] = original_link
	document['source_id'] = source_id
	document['source_name'] = source_name
	datetime_obj = datetime.strptime(entry['published'][:-4], date_format)
	document['published'] = datetime_obj.strftime('%d/%m/%Y')
	document['summary'] = summary_soup.p.text

	#pprint(document)

	# scrap original link, added browser agent to pass

	browser_request = urllibrequest.Request(original_link, headers = {'User-Agent': 'Mozilla/5.0'})
	uClient = uReq(browser_request)
	original_link_content = uClient.read()
	uClient.close()
	original_link_soup = BeautifulSoup(original_link_content, 'html.parser')

	# retrieve & save text from publication (p, ul, and blockquote)
	# InfoQ has 2 kinds of content: publication/articles and presentations

	publication_body = original_link_soup.find("div", {"class": "content-html"})
	raw_text = title

	if publication_body:
		main_image_soup = publication_body.find("img")

		if main_image_soup:
			if main_image_soup['src'].startswith("http") or main_image_soup['src'].startswith("www."):
				document['main_image'] = main_image_soup['src']
			else:
				document['main_image'] = "https://dzone.com"+main_image_soup['src']
		else:
			document['main_image'] = default_image

		for p in publication_body.findAll("p"):
			raw_text = " ".join([raw_text, p.text])
		for h in publication_body.findAll("h2"):
			raw_text = " ".join([raw_text, h.text])
		for ul in publication_body.findAll("ul"):
			raw_text = " ".join([raw_text, ul.text])

	document['raw_text'] = raw_text
	message = {}
	message['document'] = document

	#pprint(document)

	# document dict to JSON

	json_message = json.dumps(message)


	# send POST request with json_document to RAW_DATA

	http = urllib3.PoolManager()
	r = http.request('POST', 'http://raw_data:4000/api/documents', body=json_message, headers={'Content-Type': 'application/json'})

	# get id of saved document

	json_response = json.loads(r.data)
	new_doc = json_response['document']
	new_id = new_doc['id']

	# DELETE FROM FINAL VERSION
	# save message in JSON file

	with open("dataset/"+str(new_id)+"dzone1.json", 'w+') as new_json_file:
		json.dump(message, new_json_file)

	# send id to RabbitMQ

	print("New document added:  "+title)

	channel.basic_publish(exchange='', routing_key='preprocessing_queue', body=new_id)

# close connection with RabbitMQ

connection.close()

# wait X time and repeat