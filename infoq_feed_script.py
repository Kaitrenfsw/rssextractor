from bs4 import BeautifulSoup
from pprint import pprint
from datetime import datetime
from urllib.request import urlopen as uReq
import request
import feedparser

# base url and data from this source
source_name = "infoQ"
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

	document['title'] = entry['title']
	document['url'] = entry['link']
	document['source_id'] = source_id
	document['source_name'] = source_name
	document['published'] = datetime.strptime(entry['published'], date_format)
	document['main_image'] = summary_soup.img['src']
	document['summary'] = summary_soup.p.text

	pprint(document)

	# scrap original link
	# retrieve & save text from publication
	# add retrieved publication to publication list

# send publication list to RAW_DATA

# wait X time and repeat

