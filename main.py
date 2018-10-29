import os
import time

# create infinite loop to run all scripts
# leave a 5 minute window between scripts
# repeat execution after 6 hours

while True:

	print("Starting extraction...")

	# run InfoQ script

	try:
		print("Running InfoQ feed script...")
		os.system("python3 infoq_feed_script.py")
		time.sleep(300)

	except:
		print("There was a problem running InfoQ script. Skipping...")


	# run X script

	# wait and repeat

	print("Next iteration will start in 6 hours...")
	time.sleep(3600)
	print("Next iteration will start in 5 hours...")
	time.sleep(3600)
	print("Next iteration will start in 4 hours...")
	time.sleep(3600)
	print("Next iteration will start in 3 hours...")
	time.sleep(3600)
	print("Next iteration will start in 2 hours...")
	time.sleep(3600)
	print("Next iteration will start in 1 hours...")
	time.sleep(1800)
	print("Next iteration will start in 30 minutes...")
	time.sleep(900)
	print("Next iteration will start in 15 minutes...")
	time.sleep(900)




