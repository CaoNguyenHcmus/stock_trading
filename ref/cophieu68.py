#!/usr/bin/python
import requests
from bs4 import BeautifulSoup

maCK = 'DCM'
stock_url = 'http://www.cophieu68.vn/snapshot.php?id=' + maCK
print stock_url
#r = requests.get(stock_url)
r = requests.head(stock_url)
print r.headers
'''
data = r.text
soup = BeautifulSoup(data, "html.parser")
#print(soup.prettify())

## Mua
##
stockname_gm3 = soup.find('td', id="stockname_gm3").find('span').string #cell_in_table tag <td>
print stockname_gm3
stockname_klm3 = soup.find('td', id="stockname_klm3").find('span').string #cell_in_table tag <td>
print stockname_klm3
##
stockname_gm2 = soup.find('td', id="stockname_gm2").find('span').string #cell_in_table tag <td>
print stockname_gm2
stockname_klm2 = soup.find('td', id="stockname_klm2").find('span').string #cell_in_table tag <td>
print stockname_klm2
##
stockname_gm1 = soup.find('td', id="stockname_gm1").find('span').string #cell_in_table tag <td>
print stockname_gm1
stockname_klm1 = soup.find('td', id="stockname_klm1").find('span').string #cell_in_table tag <td>
print stockname_klm1

## Ban
##
stockname_gb1 = soup.find('td', id="stockname_gb1").find('span').string #cell_in_table tag <td>
print stockname_gb1
stockname_klb1 = soup.find('td', id="stockname_klb1").find('span').string #cell_in_table tag <td>
print stockname_klb1
##
stockname_gb2 = soup.find('td', id="stockname_gb2").find('span').string #cell_in_table tag <td>
print stockname_gb2
stockname_klb2 = soup.find('td', id="stockname_klb2").find('span').string #cell_in_table tag <td>
print stockname_klb2
##
stockname_gb3 = soup.find('td', id="stockname_gb3").find('span').string #cell_in_table tag <td>
print stockname_gb3
stockname_klb3 = soup.find('td', id="stockname_klb3").find('span').string #cell_in_table tag <td>
print stockname_klb3

## Tinh toan
#Mua
stockname_gm_tb = (float(stockname_gm3) + float(stockname_gm2) + float(stockname_gm1))/3.0
print "stockname_gm_tb: " + "%0.2f" % stockname_gm_tb
stockname_klm_tb = float(stockname_klm3.replace(",", "")) + float(stockname_klm2.replace(",", "")) + float(stockname_klm1.replace(",", ""))
print "stockname_klm_tb: " + "%0.0f" % stockname_klm_tb

#Ban
stockname_gb_tb = (float(stockname_gb1) + float(stockname_gb2) + float(stockname_gb3))/3.0
print "stockname_gb_tb: " + "%0.2f" % stockname_gb_tb
stockname_klb_tb = float(stockname_klb1.replace(",", "")) + float(stockname_klb2.replace(",", "")) + float(stockname_klb3.replace(",", ""))
print "stockname_klb_tb: " + "%0.0f" % stockname_klb_tb

#Phan tich kl
# Chenh lech KL dat mua - KL dat ban
cung_cau_kl_mua_ban = int(stockname_klm_tb)-int(stockname_klb_tb)
if cung_cau_kl_mua_ban > 0:
	print "cung_cau_kl_mua_ban: "+ str(cung_cau_kl_mua_ban) +  " => cau > cung => gia se tang (Xu huong ngan han)"
elif cung_cau_kl_mua_ban < 0:
	print "cung_cau_kl_mua_ban: " + str(cung_cau_kl_mua_ban) + " => cau < cung => gia se giam (Xu huong ngan han)"
else:
	print "KL cau = cung: " + str(cung_cau_kl_mua_ban)

#Phan tuc luc cau va luc ban
#Phan tich gia
#TODO
'''
#####################################################################
stock_url= 'http://s.cafef.vn/hose/DCM-cong-ty-co-phan-phan-bon-dau-khi-ca-mau.chn'
print stock_url
#r = requests.get(stock_url)
r = requests.head(stock_url)
print r.headers
'''
data = r.text
soup = BeautifulSoup(data, "html.parser")
'''