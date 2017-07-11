#!/usr/bin/python
import requests
from bs4 import BeautifulSoup

stock_url= 'http://eosscan.io'

print stock_url
r = requests.get(stock_url)

data = r.text
soup = BeautifulSoup(data, "html.parser")

####
exchanges = soup.findAll('div', {'class': "level-item has-text-centered"})
#print exchanges
#print type(exchanges[1]) # Should tag
print "####"
USD_exchange = []
for ex in exchanges[0].findAll('p'): # [USD, ETH, BTC]
	USD_exchange.append(ex.string)
print USD_exchange
Current_exchange_USD_price = USD_exchange[1] #colume 0
print "Current_exchange_USD_price: " + str(Current_exchange_USD_price)

####
print "####"
ETH_exchange = []
for ex in exchanges[1].findAll('p'): # [USD, ETH, BTC]
	ETH_exchange.append(ex.string)
print ETH_exchange
Current_exchange_ETH_price = ETH_exchange[1] #colume 1
#print "Current_exchange_ETH_price: " + str(Current_exchange_ETH_price)

####
print "####"
BTC_exchange = []
for ex in exchanges[2].findAll('p'): # [USD, ETH, BTC]
	BTC_exchange.append(ex.string)
#print BTC_exchange
Current_exchange_BTC_price = BTC_exchange[1] #colume 2
#print "Current_exchange_BTC_price: " + str(Current_exchange_BTC_price)
print "####"

####
table_row = soup.find('tr', {'class': "is-selected"})
EOSlist = []
for cells in table_row.findAll('th'):
	EOSlist.append(cells.string.replace('$', ''))

print EOSlist
Price_of_EOS_Token_ETH = EOSlist[6] #colume 5
print "Price_of_EOS_Token_ETH: " + str(Price_of_EOS_Token_ETH)

####

print "Ti gia: " + str(float(Current_exchange_ETH_price)/float(Price_of_EOS_Token_ETH))
delta = float(Current_exchange_ETH_price) - float(Price_of_EOS_Token_ETH)
percent = (delta/float(Price_of_EOS_Token_ETH)) * 100
print "ETH price - EOS token ETH = " + str(delta) + " ROI: " + str("%.2f" % percent) +"%"