import os
import time

# create infinite loop to run all scripts
# leave a 5 minute window between scripts
# repeat execution after 6 hours
testing = True

if testing:

	# testing new script

	try:
		print("Running DZone Java feed script...")
		os.system("python3 feed_scripts/dzone_java_feed_script.py")
		print("Next script will start in: 30 seconds...")
		time.sleep(10)
		print("Next script will start in: 20 seconds...")
		time.sleep(10)
		print("Next script will start in: 10 seconds...\n\n")
		time.sleep(10)

	except:
		print("There was a problem running the script. Skipping...")	

while not testing:

	print("Starting extraction...")

	# run InfoQ script

	try:
		print("Running InfoQ feed script...")
		os.system("python3 feed_scripts/infoq_feed_script.py")
		print(".....\n")
		print("Next script will start in: 30 seconds...")
		time.sleep(10)
		print("Next script will start in: 20 seconds...")
		time.sleep(10)
		print("Next script will start in: 10 seconds...\n\n")
		time.sleep(10)

	except:
		print("There was a problem running InfoQ script. Skipping...")


	# run SD Times scripts

	try:
		print("Running SD Times AI feed script...")
		os.system("python3 feed_scripts/sd_times_ai_feed_script.py")
		print("Next script will start in: 30 seconds...")
		time.sleep(10)
		print("Next script will start in: 20 seconds...")
		time.sleep(10)
		print("Next script will start in: 10 seconds...\n\n")
		time.sleep(10)

	except:
		print("There was a problem running the script. Skipping...")

	try:
		print("Running SD Times Agile feed script...")
		os.system("python3 feed_scripts/sd_times_agile_feed_script.py")
		print("Next script will start in: 30 seconds...")
		time.sleep(10)
		print("Next script will start in: 20 seconds...")
		time.sleep(10)
		print("Next script will start in: 10 seconds...\n\n")
		time.sleep(10)

	except:
		print("There was a problem running the script. Skipping...")		

	try:
		print("Running SD Times AMP feed script...")
		os.system("python3 feed_scripts/sd_times_amp_feed_script.py")
		print("Next script will start in: 30 seconds...")
		time.sleep(10)
		print("Next script will start in: 20 seconds...")
		time.sleep(10)
		print("Next script will start in: 10 seconds...\n\n")
		time.sleep(10)

	except:
		print("There was a problem running the script. Skipping...")	

	try:
		print("Running SD Times API feed script...")
		os.system("python3 feed_scripts/sd_times_api_feed_script.py")
		print("Next script will start in: 30 seconds...")
		time.sleep(10)
		print("Next script will start in: 20 seconds...")
		time.sleep(10)
		print("Next script will start in: 10 seconds...\n\n")
		time.sleep(10)

	except:
		print("There was a problem running the script. Skipping...")	

	try:
		print("Running SD Times CI/CD feed script...")
		os.system("python3 feed_scripts/sd_times_cicd_feed_script.py")
		print("Next script will start in: 30 seconds...")
		time.sleep(10)
		print("Next script will start in: 20 seconds...")
		time.sleep(10)
		print("Next script will start in: 10 seconds...\n\n")
		time.sleep(10)

	except:
		print("There was a problem running the script. Skipping...")	

	try:
		print("Running SD Times Containers feed script...")
		os.system("python3 feed_scripts/sd_times_containers_feed_script.py")
		print("Next script will start in: 30 seconds...")
		time.sleep(10)
		print("Next script will start in: 20 seconds...")
		time.sleep(10)
		print("Next script will start in: 10 seconds...\n\n")
		time.sleep(10)

	except:
		print("There was a problem running the script. Skipping...")	

	try:
		print("Running SD Times Data feed script...")
		os.system("python3 feed_scripts/sd_times_data_feed_script.py")
		print("Next script will start in: 30 seconds...")
		time.sleep(10)
		print("Next script will start in: 20 seconds...")
		time.sleep(10)
		print("Next script will start in: 10 seconds...\n\n")
		time.sleep(10)

	except:
		print("There was a problem running the script. Skipping...")	

	try:
		print("Running SD Times DevOps feed script...")
		os.system("python3 feed_scripts/sd_times_devops_feed_script.py")
		print("Next script will start in: 30 seconds...")
		time.sleep(10)
		print("Next script will start in: 20 seconds...")
		time.sleep(10)
		print("Next script will start in: 10 seconds...\n\n")
		time.sleep(10)

	except:
		print("There was a problem running the script. Skipping...")	

	try:
		print("Running SD Times DevSecOps feed script...")
		os.system("python3 feed_scripts/sd_times_devsecops_feed_script.py")
		print("Next script will start in: 30 seconds...")
		time.sleep(10)
		print("Next script will start in: 20 seconds...")
		time.sleep(10)
		print("Next script will start in: 10 seconds...\n\n")
		time.sleep(10)

	except:
		print("There was a problem running the script. Skipping...")	


	# run The Hacker News script

	try:
		print("Running The Hacerk News feed script...")
		os.system("python3 feed_scripts/the_hacker_news_feed_script.py")
		print("Next script will start in: 30 seconds...")
		time.sleep(10)
		print("Next script will start in: 20 seconds...")
		time.sleep(10)
		print("Next script will start in: 10 seconds...\n\n")
		time.sleep(10)

	except:
		print("There was a problem running the script. Skipping...")

	# run DZone scripts:

	try:
		print("Running DZone AI feed script...")
		os.system("python3 feed_scripts/dzone_ai_feed_script.py")
		print("Next script will start in: 30 seconds...")
		time.sleep(10)
		print("Next script will start in: 20 seconds...")
		time.sleep(10)
		print("Next script will start in: 10 seconds...\n\n")
		time.sleep(10)

	except:
		print("There was a problem running the script. Skipping...")

	try:
		print("Running DZone Agile feed script...")
		os.system("python3 feed_scripts/dzone_agile_feed_script.py")
		print("Next script will start in: 30 seconds...")
		time.sleep(10)
		print("Next script will start in: 20 seconds...")
		time.sleep(10)
		print("Next script will start in: 10 seconds...\n\n")
		time.sleep(10)

	except:
		print("There was a problem running the script. Skipping...")	

	try:
		print("Running DZone Big Data feed script...")
		os.system("python3 feed_scripts/dzone_bigdata_feed_script.py")
		print("Next script will start in: 30 seconds...")
		time.sleep(10)
		print("Next script will start in: 20 seconds...")
		time.sleep(10)
		print("Next script will start in: 10 seconds...\n\n")
		time.sleep(10)

	except:
		print("There was a problem running the script. Skipping...")	

	try:
		print("Running DZone Cloud feed script...")
		os.system("python3 feed_scripts/dzone_cloud_feed_script.py")
		print("Next script will start in: 30 seconds...")
		time.sleep(10)
		print("Next script will start in: 20 seconds...")
		time.sleep(10)
		print("Next script will start in: 10 seconds...\n\n")
		time.sleep(10)

	except:
		print("There was a problem running the script. Skipping...")	

	try:
		print("Running DZone Database feed script...")
		os.system("python3 feed_scripts/dzone_database_feed_script.py")
		print("Next script will start in: 30 seconds...")
		time.sleep(10)
		print("Next script will start in: 20 seconds...")
		time.sleep(10)
		print("Next script will start in: 10 seconds...\n\n")
		time.sleep(10)

	except:
		print("There was a problem running the script. Skipping...")

	try:
		print("Running DZone DevOps feed script...")
		os.system("python3 feed_scripts/dzone_devops_feed_script.py")
		print("Next script will start in: 30 seconds...")
		time.sleep(10)
		print("Next script will start in: 20 seconds...")
		time.sleep(10)
		print("Next script will start in: 10 seconds...\n\n")
		time.sleep(10)

	except:
		print("There was a problem running the script. Skipping...")	

	try:
		print("Running DZone Integration feed script...")
		os.system("python3 feed_scripts/dzone_integration_feed_script.py")
		print("Next script will start in: 30 seconds...")
		time.sleep(10)
		print("Next script will start in: 20 seconds...")
		time.sleep(10)
		print("Next script will start in: 10 seconds...\n\n")
		time.sleep(10)

	except:
		print("There was a problem running the script. Skipping...")

	try:
		print("Running DZone IoT feed script...")
		os.system("python3 feed_scripts/dzone_iot_feed_script.py")
		print("Next script will start in: 30 seconds...")
		time.sleep(10)
		print("Next script will start in: 20 seconds...")
		time.sleep(10)
		print("Next script will start in: 10 seconds...\n\n")
		time.sleep(10)

	except:
		print("There was a problem running the script. Skipping...")	

	try:
		print("Running DZone Java feed script...")
		os.system("python3 feed_scripts/dzone_java_feed_script.py")
		print("Next script will start in: 30 seconds...")
		time.sleep(10)
		print("Next script will start in: 20 seconds...")
		time.sleep(10)
		print("Next script will start in: 10 seconds...\n\n")
		time.sleep(10)

	except:
		print("There was a problem running the script. Skipping...")	

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




