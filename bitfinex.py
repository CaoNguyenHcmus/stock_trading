#!/usr/bin/python
import requests
import json

# buy_price, target_price(+5%), stop_loss_price(-10%) based on Excel or Blockfolio s/w
expect_dict = 	{'btcusd': [2000, 0.05, 0.1],
				'eosusd':[90.0, 0.05, 0.1]}

####
# Symbols
####
url = "https://api.bitfinex.com/v1/symbols"
response = requests.request("GET", url)

#print(response.text)

####
# Ticker
####
print "btcusd"
url = "https://api.bitfinex.com/v1/pubticker/btcusd"

btcusd_ticker = []
response = requests.request("GET", url)
# debug
btcusd_ticker = response.json() # Convert <class 'requests.models.Response'> to Json
#print type(btcusd_ticker)

print btcusd_ticker
print "mid: " + btcusd_ticker["mid"]
print "last_price: " + btcusd_ticker["last_price"]

change_price = float(btcusd_ticker["mid"]) - float(btcusd_ticker["last_price"])
change_percent = (change_price/float(btcusd_ticker["mid"]))*100

print "change_price: " + str(change_price),
print "change_percent: " + str(change_percent)

print "=> expected_price: " + str(expect_dict['btcusd'][0])
price_down = float(btcusd_ticker["mid"]) - expect_dict['btcusd'][0]
print price_down
#price_up = 

print "####"
print "eosusd"
url = "https://api.bitfinex.com/v1/pubticker/eosusd"

btcusd_ticker = []
response = requests.request("GET", url)
eosusd_ticker = response.json() # Convert <class 'requests.models.Response'> to Json

#print eosusd_ticker
print "mid: " + eosusd_ticker["mid"]
print "last_price: " + eosusd_ticker["last_price"]
change_price = float(eosusd_ticker["mid"]) - float(eosusd_ticker["last_price"])
print "change_price: " + str(change_price)