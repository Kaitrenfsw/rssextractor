from datetime import datetime
from threading import Timer
import feedparser
import pika
import re
import json


consulted_pages = ["https://www.reddit.com/r/python/.rss?limit=20"]

x=datetime.today()
y=x.replace(day=x.day, hour=x.hour, minute=x.minute+1, second=0, microsecond=0)
delta_t=y-x

secs=delta_t.seconds+1

def cleanhtml(raw_html):
  cleanr = re.compile('<.*?>')
  cleantext = re.sub(cleanr, '', raw_html)
  return cleantext

def daily_refreshment():
	for consulted_page in consulted_pages:
		today = datetime.today()
		yesterday = today.replace(day=today.day - 1, hour=1, minute=0, second=0, microsecond=0)

		d = feedparser.parse(consulted_page, modified = yesterday)
		for post in d.entries:
			print(post.title)

	x=datetime.today()
	y=x.replace(day=x.day, hour=x.hour, minute=x.minute+1, second=0, microsecond=0)
	delta_t=y-x
	secs=delta_t.seconds+1
	t = Timer(secs, daily_refreshment)
	t.start()


def get_rss_content(page):
	pass

connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq-docker'))
channel = connection.channel()
channel.queue_declare(queue='hello')


for consulted_page in consulted_pages:

	d = feedparser.parse(consulted_page)
	message = d.entries[0].title
	response = {}
	response["date"] = datetime.today().strftime("%Y-%m-%d")
	response["documents"] = []
	documents = []
	doc_count = 0
	for post in d.entries:
		post_response = feedparser.parse(post.url + '/.rss')
		message = ''
		
		post_corpus = {}
		for post_content in post_response.entries:

			print(cleanhtml( post_content['content'][0]['value'] ))
			message = message + cleanhtml(post_content['content'][0]['value'])


		post_corpus['text'] = message
		post_corpus['title'] = post.title
		post_corpus['url'] = post.url
		post_corpus['site'] = consulted_page
		post_corpus['site_name'] = consulted_page
		post_corpus['published'] = datetime.today().strftime("%Y-%m-%d")

		response["documents"].append(post_corpus)

		doc_count += 1

	response["doc_count"] = doc_count
	print(response)
	response = json.dumps(response)
	channel.basic_publish(exchange='',
	                      routing_key='hello',
	                      body=response)

import pika



t = Timer(secs, daily_refreshment)
t.start()
