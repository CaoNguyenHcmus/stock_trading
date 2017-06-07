#!/usr/bin/python
import sys # for exit
from bs4 import BeautifulSoup
import requests
import re
import time
import argparse

from termcolor import colored

# buy_price, target_price(+5%), stop_loss_price(-10%)
expect_dict = {'MSN': [42.84, 0.05, 0.1] ,'LHG': [19.7, 0.05, 0.1], 'QNS':[90.0, 0.05, 0.1], 'HD2': [14.3, 0.05, 0.1], 'HID': [4.32, 0.05, 0.1], 'HVG': [7.3, 0.05, 0.1], 'TYA': [11.279, 0.05, 0.1]}

def displayStock( stock_url, is_predict ):
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
	# class="dltlu-nochange orange"
	# class="dltlu-down red"
	# class="dltlu-up green"
	#print tag_down
	quoted_pattern = re.findall(r'"[^"]*"', str(tag_down))
	wordList = str(quoted_pattern).split()
	trend = re.findall(r'\w+', str(wordList[0]))
	color = re.findall(r'\w+', str(wordList[1]))
	if color[0] == "orange":	# termcolor don't support "orange" color => use "yellow" color to replace
		color[0] = "yellow"
#	print "trend: " + str(trend[1])
#	print "color: " + str(color[0])

	# Convert List to String
	#str1 = ''.join(str(e) for e in tag_down)
	#print str1
	str2 = ''.join(tag_down[1])
#	print str2
#	print str2.lstrip()

	pattern = re.compile(r'\s+')
	sentence = re.sub(pattern, '\t', str2.lstrip())
#	print sentence
	#print soup.title.string.lstrip()[0:3] + "\t" + tag_point[0] + "\t"+ sentence + "\t",
#	print colored('hello', 'red'), colored('world', 'green')
	print soup.title.string.lstrip()[0:3] + "\t" + colored(tag_point[0], color[0]) + "\t"+ colored(sentence, color[0]) + "\t",

#	Predict & compare target value here
	MaCK = soup.title.string.lstrip()[0:3]
	GiaHT = tag_point[0]
	for key, values in expect_dict.iteritems():
		if MaCK == key:
#			print MaCK + "\t" +str(expect_dict[key])
			buy_price = expect_dict[key][0]
			target_price = float(buy_price) + (float(buy_price) * float(expect_dict[key][1]))
			stop_loss_price = float(buy_price) - (float(buy_price) * float(expect_dict[key][2]))
			percent_Lai_Lo = ((float(GiaHT) - float(buy_price))*100)/float(buy_price)
			# Overal Color
			if percent_Lai_Lo > 0.0:
				#print "Lon hon 0"
				Scolor = "green"
			elif percent_Lai_Lo < 0.0:
				#print "Nho hon 0"
				Scolor = "red"
			elif percent_Lai_Lo == 0.0:
				#print "Bang 0"
				Scolor = "yellow"

			if is_predict is True: # predict_message enable
				print "Return/Loss:" + " "+ colored(str(("%.2f" % percent_Lai_Lo))+"%", Scolor)+"\t",
				# predict message is optional
				predict_message = ""
				if ( float(GiaHT) >= float(target_price) ) : predict_message = " => [GOOD] >= target price(+5%) => SELL"
				elif ( float(stop_loss_price) < float(GiaHT) < float(buy_price) ) : predict_message = " => [lower price] cut-loss " + str(("%.2f" % stop_loss_price)) + "[-10%]"
				elif ( float(buy_price) < float(GiaHT) < float(target_price) ) : predict_message = " => [higher price] target " + str(("%.2f" % target_price)) + "[+5%]"
				elif ( float(GiaHT) <= float(stop_loss_price) ) : predict_message = " => [WARNING] CUT-LOSS"
				#print "buy_price:" + " "+ str(buy_price) + " "+ "target_price:" + " "+ str(target_price) + " "+ "stop_loss_price:" + " "+ str(stop_loss_price) + predict_message
				print predict_message
			else:
				print "Return/Loss:" + " "+ colored(str(("%.2f" % percent_Lai_Lo))+"%", Scolor)+"\t"

def mainProcess( is_watchlist, is_predict ):
	#count = 0
	#while (count < 1):
		#print 'The count is:', count
		#count = count + 1
	print "The time of maximum pessimism is the best time to buy"
	print "and the time of maximum optimism is the best time to sell."
	with open('stock_url.txt') as f:
		for stock_url in f.read().splitlines():
		#		print lines
			displayStock(stock_url, is_predict)
	f.close() 
		# Wait for 5 seconds
	#	time.sleep(3)

	print "Good bye!"

##
## MAIN
##
is_watchlist = False
is_predict = False
#
# Create option parser
#

parser = argparse.ArgumentParser(description="Stock trading script")

# action
parser.add_argument("-w", "--watchlist", help='display watch list', action="store_true")
parser.add_argument("-p", "--predict", help='display watch list and predict message', action="store_true")

args = parser.parse_args()

if args.watchlist:
#	print "watchlist = %s" % args.watchlist
	is_watchlist = True
if args.predict:
#	print "predict = %s" % args.predict
	is_predict = True


if is_watchlist is True:
	mainProcess( is_watchlist, is_predict )
else:
	parser.print_help()
	sys.exit(0)