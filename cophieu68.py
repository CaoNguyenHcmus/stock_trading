#!/usr/bin/python
import requests
from bs4 import BeautifulSoup
import re
import sys # for exit

from termcolor import colored

###
def isColor( value, ref ):
	color = "while" #default color
	if value > ref:
		#print "Lon hon 0"
		color = "green"
	elif value < ref:
		#print "Nho hon 0"
		color = "red"
	elif value == ref:
		#print "Bang 0"
		color = "yellow"
	return color
###

###############################################################################################
#TODO
#warning_gia = +1% or -1%
#warning_kl = vuot khoi luong hom truoc la canh bao
###############################################################################################
#handle input from database file
# Idea: User only input maCK ==> program will generate stock url on cafef and cophieu68
#maCK = 'QNS'
#maCK = 'MSN'
maCK = raw_input("Enter maCK: ")
stock_url = ''
with open('database.txt') as f:
	for stock_urls in f.read().splitlines():
#			print stock_urls
			result = stock_urls.find(maCK)			
			if result < 0:
				pass
			else: #found
				stock_url = stock_urls
f.close()

if stock_url == '':
	print "maCK not found in database!!"
	sys.exit(0)
#print "Result: " + stock_url

###############################################################################################
#stock_url= 'http://s.cafef.vn/upcom/HD2-ctcp-dau-tu-phat-trien-nha-hud2.chn' #for debug

# Create a list of each bit between slashes
slashparts = stock_url.split('/')
# Now join back the first three sections 'http:', '' and 'example.com'
#basename = '/'.join(slashparts[:3]) + '/'
#print slashparts
#print slashparts[len(slashparts)-2] # San giao dich
maCK = slashparts[len(slashparts)-1][:3] # get ending part and get 3 character

'''#for debug
if maCK:
	print maCK
else:
	print "maCK not found!!"
'''
#print stock_url
r = requests.get(stock_url)

#r = requests.head(stock_url)
#print r.headers
data = r.text
soup = BeautifulSoup(data, "html.parser")
#print(soup.prettify())




#====
list_dltp_price = []
dltp_price = soup.find("div", {"class" : "dltl-price"}).find('ul')
for li_tag in dltp_price.findAll('li'):
	li = li_tag.find("div", {"class" : "right"})
	if li != None:
		#print li.string.split()[0]
		list_dltp_price.append(li.string.split()[0])
		#print "++++"
#print list_dltp_price
gia_mo_cua = list_dltp_price[0]
gia_cao_nhat = list_dltp_price[1]
gia_thap_nhat = list_dltp_price[2]
KL_GDNN = list_dltp_price[3]
Room_NN_con_lai = list_dltp_price[4]
#Room_NN_con_lai = list_dltp_price[5]
#print "gia_mo_cua: " + gia_mo_cua
#print "gia_cao_nhat: " + gia_cao_nhat
#print "gia_thap_nhat: " + gia_thap_nhat

print "KL_GDNN: " + KL_GDNN

#print "Room_NN_con_lai: " + Room_NN_con_lai
##############################
divData1LichSu = soup.find('div', {"id": "divData1LichSu"})
tblData1LichSu = divData1LichSu.find('table')
#print tblData1LichSu
#list
ngay = [];
thay_doi_gia = [];
KLkhop_lenh = [];
tongKLGD = [];
for table_row in tblData1LichSu.findAll('tr'):
	#print "=============="
	cells = table_row.findAll('td')
	if len(cells) > 0:
		ngay.append(cells[0].string)
		thay_doi_gia.append(cells[1].contents)
		KLkhop_lenh.append(cells[2].string)
		tongKLGD.append(cells[3].string)
''' #begin print data in table
		print "ngay: " + cells[0].string
		print cells[1].contents
		print "KLkhop_lenh: " + cells[2].string
		print "tongKLGD: " + cells[3].string
		print "===="
print ngay
print thay_doi_gia
print KLkhop_lenh
print tongKLGD
''' # end print data in table
#print "KL_previous_day: " + KLkhop_lenh[0]

gia_tham_chieu = soup.find('div', id="REF").string.split() # REF
#print "gia_tham_chieu" + str(gia_tham_chieu)

#'''
###############################################################################################
#maCK = 'QNS'
#maCK = raw_input("Enter maCK: ")
stock_url = 'http://www.cophieu68.vn/snapshot.php?id=' + maCK
#print stock_url #for debug
r = requests.get(stock_url)

data = r.text
soup = BeautifulSoup(data, "html.parser")
#print(soup.prettify())

## Mua
##
stockname_gm3 = soup.find('td', id="stockname_gm3").find('span').string #cell_in_table tag <td>

stockname_klm3 = soup.find('td', id="stockname_klm3").find('span').string #cell_in_table tag <td>

##
stockname_gm2 = soup.find('td', id="stockname_gm2").find('span').string #cell_in_table tag <td>

stockname_klm2 = soup.find('td', id="stockname_klm2").find('span').string #cell_in_table tag <td>

##
stockname_gm1 = soup.find('td', id="stockname_gm1").find('span').string #cell_in_table tag <td>

stockname_klm1 = soup.find('td', id="stockname_klm1").find('span').string #cell_in_table tag <td>


## Ban
##
stockname_gb1 = soup.find('td', id="stockname_gb1").find('span').string #cell_in_table tag <td>

stockname_klb1 = soup.find('td', id="stockname_klb1").find('span').string #cell_in_table tag <td>

##
stockname_gb2 = soup.find('td', id="stockname_gb2").find('span').string #cell_in_table tag <td>

stockname_klb2 = soup.find('td', id="stockname_klb2").find('span').string #cell_in_table tag <td>

##
stockname_gb3 = soup.find('td', id="stockname_gb3").find('span').string #cell_in_table tag <td>

stockname_klb3 = soup.find('td', id="stockname_klb3").find('span').string #cell_in_table tag <td>

## Tinh toan
#Mua
stockname_gm_tb = (float(stockname_gm3) + float(stockname_gm2) + float(stockname_gm1))/3.0
#print "stockname_gm_tb: " + "%0.2f" % stockname_gm_tb
stockname_klm_tb = float(stockname_klm3.replace(",", "")) + float(stockname_klm2.replace(",", "")) + float(stockname_klm1.replace(",", ""))
#print "stockname_klm_tb: " + "%0.0f" % stockname_klm_tb

#Ban
stockname_gb_tb = (float(stockname_gb1) + float(stockname_gb2) + float(stockname_gb3))/3.0
#print "stockname_gb_tb: " + "%0.2f" % stockname_gb_tb
stockname_klb_tb = float(stockname_klb1.replace(",", "")) + float(stockname_klb2.replace(",", "")) + float(stockname_klb3.replace(",", ""))
#print "stockname_klb_tb: " + "%0.0f" % stockname_klb_tb

#TODO: print color
print "Mua(Gia/KL): \t" + stockname_gm3 +"\t"+ stockname_klm3 +"\t"+ stockname_gm2  +"\t"+ stockname_klm2 +"\t"+ stockname_gm1 +"\t"+ stockname_klm1 
print "Ban(Gia/KL): \t" + stockname_gb1 +"\t"+ stockname_klb1 +"\t"+ stockname_gb2 +"\t"+ stockname_klb2 +"\t"+ stockname_gb3 +"\t"+ stockname_klb3
print "=> gm_tb: " + "%0.2f" % stockname_gm_tb + "\tklm_tb: " + "%0.0f" % stockname_klm_tb + "\tgb_tb: " + "%0.2f" % stockname_gb_tb + "\tklb_tb: " + "%0.0f" % stockname_klb_tb

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


####
stockname_close = soup.find('strong', id="stockname_close").string # Gia hien tai tag <strong>
#print "Gia hien tai: " + stockname_close,
stockname_change = soup.find('strong', id="stockname_change").find('span').string.split() # Gia hien tai tag <strong>
#print "Thay doi: " + stockname_change

color_stockname_close = isColor(float(stockname_close), float(gia_tham_chieu[0]))
print color_stockname_close

print "Gia hien tai: " + colored(str(stockname_close), color_stockname_close) + "\t"+ colored(str(stockname_change), color_stockname_close)
###
stockname_volume = soup.find('strong', id="stockname_volume").find('span').string #cell_in_table tag <td>
print "KL hien tai: " + stockname_volume + "\t", 
print "KL_previous_day: " + KLkhop_lenh[0]
# delta = KLkhop_lenh previous day - KLkhop_lenh hien tai
delta = int(KLkhop_lenh[0].replace(",", "")) - int(stockname_volume.replace(",", ""))
if delta > 0:
	print "Nho hon khoi luong ngay hom truoc: ", 
	print (delta * 100)/int(KLkhop_lenh[0].replace(",", "")),
	print "%"
elif delta == 0:
	print "KL hien tai = KL previous day ==> Theo doi ky"
else:
	print "Canh bao vuot qua khoi luong hom truoc(%): ", 
	print (abs(delta) * 100)/int(stockname_volume.replace(",", ""))

stockname_price_lowest = soup.find('strong', id="stockname_price_lowest").find('span').string #cell_in_table tag <td>
#print "stockname_price_lowest hien tai: " + stockname_price_lowest,

stockname_price_highest = soup.find('strong', id="stockname_price_highest").find('span').string #cell_in_table tag <td>
#print "stockname_price_highest hien tai: " + stockname_price_highest


#'''
###############################################################################################


''' Du lieu lich su trong ngay (Luu y trong nay no co ve ra cai bieu do luon)
tableDataLichSu = soup.find("div", {"id": "trade_detail"}).contents #cell_in_table tag <td>
print tableDataLichSu
'''