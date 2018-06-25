from datetime import datetime
from threading import Timer
import feedparser
import pika


consulted_pages = ["https://www.reddit.com/r/python/.rss?limit=100"]

x=datetime.today()
y=x.replace(day=x.day, hour=x.hour, minute=x.minute+1, second=0, microsecond=0)
delta_t=y-x

secs=delta_t.seconds+1

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
	print(len(d['entries']))
	message = d.entries[0].title
	print(message)
	channel.basic_publish(exchange='',
	                      routing_key='hello',
	                      body=message)


	for post in d.entries:
		print(post.title)
		print("----------------")

import pika



print("hello")
t = Timer(secs, daily_refreshment)
t.start()

