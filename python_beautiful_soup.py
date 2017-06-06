#!/usr/bin/python
#Installation
#sudo apt-get install python-bs4
from bs4 import BeautifulSoup
import requests
import re
import time

def displayStock( stock_url ):
	r = requests.get(stock_url)
	#r = requests.get(lhg_url)

	data = r.text
	soup = BeautifulSoup(data)

	# Ma
#	print soup.title.string.lstrip()[0:3]

	# Gia //List type
	tag_point=soup.find("div", {"class" : "dltlu-point"}).contents
#	print tag_point[0] ## Print first character

	# Tang/giam //List type
	tag_down=soup.find(id="CC").contents

	# Convert List to String
	#str1 = ''.join(str(e) for e in tag_down)
	#print str1
	str2 = ''.join(tag_down[1])
#	print str2.lstrip()

	print soup.title.string.lstrip()[0:3] + "\t" + tag_point[0] + "\t"+ str2
	#print re.findall(r'\d+', str2) #Not correct now

# main
count = 0
while (count < 1):
	print 'The count is:', count
	count = count + 1
   	with open('stock_url.txt') as f:
		for lines in f.read().splitlines():
	#		print lines
			displayStock(lines)
	f.close() 
	# Wait for 5 seconds
	time.sleep(3)

print "Good bye!"