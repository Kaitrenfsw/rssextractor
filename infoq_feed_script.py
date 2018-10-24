from bs4 import BeautifulSoup
from pprint import pprint
from datetime import datetime
from urllib.request import urlopen as uReq
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
source_name = "InfoQ"
source_id = 1
rss_url= "https://feed.infoq.com/"
date_format = '%a, %d %b %Y %X %Z'
d = feedparser.parse(rss_url)

# list of rss entries
entries = d['entries']

# check last recorded entry -- create record file text if it does not exist

# create empty publication list

documents = {"documents": [ ]}

# get data from non-recorded entries and original links to publications

for entry in entries:

	# scrap html embeded summary

	summary = entry['summary']
	summary_soup = BeautifulSoup(summary, 'html.parser')

	# empty dictionary to save entry data
	
	document = {}
	
	# stop loop if entry is already recorded

	# save base data (title, p_date, url, image, source_id, source_name, summary[if-any])

	title = entry['title']
	document['title'] = title
	original_link = entry['link']
	document['url'] = original_link
	document['source_id'] = source_id
	document['source_name'] = source_name
	datetime_obj = datetime.strptime(entry['published'], date_format)
	document['published'] = datetime_obj.strftime('%d/%m/%Y')
	document['main_image'] = summary_soup.img['src']
	document['summary'] = summary_soup.p.text

	#pprint(document)

	# scrap original link

	uClient = uReq(original_link)
	original_link_content = uClient.read()
	uClient.close()
	original_link_soup = BeautifulSoup(original_link_content, 'html.parser')

	# retrieve & save text from publication (p, ul, and blockquote)
	# InfoQ has 2 kinds of content: publication/articles and presentations

	publication_body = original_link_soup.find("div", {"class": "text_info"})
	presentation_body = original_link_soup.find("p", {"id": "summary"})
	raw_text = title

	if publication_body:
		for p in publication_body.findAll("p", recursive=False):
			raw_text = " ".join([raw_text, p.text])
		for ul in publication_body.findAll("ul", recursive=False):
			raw_text = " ".join([raw_text, ul.text])
		for bq in publication_body.findAll("blockquote", recursive=False):
			raw_text = " ".join([raw_text, bq.text])

	if presentation_body:
		raw_text = " ".join([raw_text, presentation_body.text]) 

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

	# send id to RabbitMQ

	channel.basic_publish(exchange='', routing_key='preprocessing_queue', body=new_id)

# close connection with RabbitMQ

connection.close()

# wait X time and repeat

