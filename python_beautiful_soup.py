#!/usr/bin/python
from bs4 import BeautifulSoup
import requests
import re
import time

# Will be improvement
# target_price, stop_loss_price
expect_dict = {'MSN': [44.1, 0] ,'LHG': [19.9, 0], 'QNS':[100.0, 0], 'HD2': [13.9, 0], 'HID': [4.13, 0], 'HVG': [7.25, 0], 'TYA': [12.4, 0]}

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
#	print str2
#	print str2.lstrip()

	pattern = re.compile(r'\s+')
	sentence = re.sub(pattern, '\t', str2.lstrip())
#	print sentence
	print soup.title.string.lstrip()[0:3] + "\t" + tag_point[0] + "\t"+ sentence + "\t",

#	Predict & compare target value here
	MaCK = soup.title.string.lstrip()[0:3]
	GiaHT = tag_point[0]
	for key, values in expect_dict.iteritems():
		if MaCK == key:
#			print MaCK + "\t" +str(expect_dict[key])
			target_price = expect_dict[key][0]
			stop_loss_price = expect_dict[key][1]
			predict_message = ""
			if ( float(target_price) > float(GiaHT) ) : predict_message = " => Vuot qua ky vong, theo doi"
			elif ( float(target_price) == float(GiaHT) ) : predict_message = " => Bang gia ky vong, ban"
			elif ( float(target_price) < float(GiaHT) ) : predict_message = " => Thap hon gia ky vong, theo doi"
			elif ( float(stop_loss_price) >= float(GiaHT) ) : predict_message = " => Cut-loss"
			print "target_price:" + " "+ str(target_price) + " "+ "stop_loss_price:" + " "+ str(stop_loss_price) + predict_message
			#print "target_price" + " "+ str(target_price) + "Gia Hien Tai" + " "+ str(GiaHT) + "=>"+ predict_message

# main
#count = 0
#while (count < 1):
	#print 'The count is:', count
	#count = count + 1
print "The time of maximum pessimism is the best time to buy"
print "and the time of maximum optimism is the best time to sell."
with open('stock_url.txt') as f:
	for stock_url in f.read().splitlines():
	#		print lines
		displayStock(stock_url)
f.close() 
	# Wait for 5 seconds
#	time.sleep(3)

print "Good bye!"