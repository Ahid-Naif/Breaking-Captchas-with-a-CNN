import requests
import time
import os

outputPath = ""
numImages  = 505 

# initialize the URL that contains the captcha images that we will
# be downloading along with the total number of images downloaded
# thus far
url = "https://www.e-zpassny.com/vector/jcaptcha.do"
total = 0

# loop over the number of images to download
for i in range(0, numImages):
	try:
		# try to grab a new captcha image
		r = requests.get(url, timeout=60)

		# save the image to disk
		p = os.path.sep.join([outputPath, "{}.jpg".format(
			str(total).zfill(5))])
		f = open(p, "wb")
		f.write(r.content)
		f.close()

		# update the counter
		print("[INFO] downloaded: {}".format(p))
		total += 1

	# handle if any exceptions are thrown during the download process
	except:
		print("[INFO] error downloading image...")

	# insert a small sleep to be courteous to the server
	time.sleep(0.1)