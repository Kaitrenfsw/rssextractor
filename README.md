# RSS extractor script collection
Python 3.6.1
* BeautifulSoup 4

Each script is associated with a corresponding source.

## Main script (TO-DO):
### Name: main.py

This script execute all other scripts.

## InfoQ:
### Name: infoq_feed_script.py

This script retrieves publications from the InfoQ RSS feed.
It uses the file infoq_record.txt to keep track of last retrieved publication.
InfoQ does not have historical data.

## Message format:

All scripts send retrieved publications, one-by-one, to RAW_DATA service with the following format:
```
	{
		"document" : 
			{
				“title”: <STRING>
				“url”: <STRING>
				“source_id”: <NUMBER>
				“source_name”: <CATEGORY>
				“published”: <DATE>
				“main_image”: <STRING>
				“raw_text”: <STRING>
				“summary”: <STRING>

			}
	}
```

