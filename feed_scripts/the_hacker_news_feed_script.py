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
source_name = "The Hacker News"
source_id = 3
rss_url= "https://feeds.feedburner.com/TheHackersNews?format=xml"
date_format = '%a, %d %b %Y %X'
first_exec = False

# check if file exist and set 'first_exec' var

dir_path = "feed_logs/"
file_name = "the_hacker_news_feed_log.txt"

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
	original_link = entry['feedburner_origlink']
	document['url'] = original_link
	document['source_id'] = source_id
	document['source_name'] = source_name
	datetime_obj = datetime.strptime(entry['published'][:-4], date_format)
	document['published'] = datetime_obj.strftime('%d/%m/%Y')
	document['summary'] = summary_soup.text

	#pprint(document)

	# scrap original link, added browser agent to pass

	browser_request = urllibrequest.Request(original_link, headers = {'User-Agent': 'Mozilla/5.0'})
	uClient = uReq(browser_request)
	original_link_content = uClient.read()
	uClient.close()
	original_link_soup = BeautifulSoup(original_link_content, 'html.parser')

	# retrieve & save text from publication (p, ul, and blockquote)
	# InfoQ has 2 kinds of content: publication/articles and presentations

	publication_body = original_link_soup.find("div", {"class": "articlebody"})
	raw_text = title

	if publication_body:
		separator_soup = publication_body.find("div", {"class": "separator"})
		main_image_soup = separator_soup.find("img")
		content_soup = publication_body.find("div", recursive=False)

		if main_image_soup:
			document['main_image'] = main_image_soup['src']
		else:
			document['main_image'] = ''
		for text_piece in content_soup.findAll(text=True, recursive=False):
			raw_text = " ".join([raw_text, text_piece])
		for a in content_soup.findAll("a", recursive=False):
			raw_text = " ".join([raw_text, a.text])
		for ul in content_soup.findAll("ul", recursive=False):
			raw_text = " ".join([raw_text, ul.text])
		for bq in content_soup.findAll("blockquote"):
			raw_text = " ".join([raw_text, bq.text])

	#if presentation_body:
		#raw_text = " ".join([raw_text, presentation_body.text]) 

	document['raw_text'] = raw_text
	message = {}
	message['document'] = document

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

	with open("dataset/"+str(new_id)+"sdtimes.json", 'w+') as new_json_file:
		json.dump(message, new_json_file)

	# send id to RabbitMQ

	print("New document added:  "+title)

	channel.basic_publish(exchange='', routing_key='preprocessing_queue', body=new_id)

# close connection with RabbitMQ

connection.close()

# wait X time and repeat