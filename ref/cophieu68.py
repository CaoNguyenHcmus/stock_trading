#!/usr/bin/python
import requests
from bs4 import BeautifulSoup

maCK = 'HD2'
maCK = raw_input("Enter maCK: ")
stock_url = 'http://www.cophieu68.vn/snapshot.php?id=' + maCK
print stock_url
r = requests.get(stock_url)
'''
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


####
stockname_close = soup.find('strong', id="stockname_close").string # Gia hien tai tag <strong>
print "Gia hien tai: " + stockname_close,

stockname_change = soup.find('strong', id="stockname_change").find('span').string.split() # Gia hien tai tag <strong>
print stockname_change
#print "Thay doi: " + stockname_change

stockname_ref = float(stockname_close) - float(stockname_change[0])
print "Gia tham chieu: " + str(stockname_ref)
###
stockname_volume = soup.find('strong', id="stockname_volume").find('span').string #cell_in_table tag <td>
print "stockname_volume hien tai: " + stockname_volume

stockname_price_lowest = soup.find('strong', id="stockname_price_lowest").find('span').string #cell_in_table tag <td>
print "stockname_price_lowest hien tai: " + stockname_price_lowest,

stockname_price_highest = soup.find('strong', id="stockname_price_highest").find('span').string #cell_in_table tag <td>
print "stockname_price_highest hien tai: " + stockname_price_highest

''' Du lieu lich su trong ngay (Luu y trong nay no co ve ra cai bieu do luon)
tableDataLichSu = soup.find("div", {"id": "trade_detail"}).contents #cell_in_table tag <td>
print tableDataLichSu
'''
#'divData1LichSu'


historyprice_url='http://www.cophieu68.vn/historyprice.php?id=' + maCK
print historyprice_url
r = requests.get(historyprice_url)
'''
r = requests.head(stock_url)
print r.headers
'''
data = r.text
#print data
soup = BeautifulSoup(data, "html.parser")
#print(soup.prettify())
#tableDataLichSu = soup.find("div", {"id": "content"}).contents #cell_in_table tag <td>

table = soup.find('table', attrs={'class':'stock'})
#print table
#https://gist.github.com/phillipsm/0ed98b2585f0ada5a769
for table_row in table.findAll('tr'):
	print table_row
'''
rows = table.find_all('tr')
print rows
'''

'''
for row in rows:
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    data.append([ele for ele in cols if ele]) # Get rid of empty values
'''


'''
#####################################################################
stock_url= 'http://s.cafef.vn/hose/DCM-cong-ty-co-phan-phan-bon-dau-khi-ca-mau.chn'
print stock_url
r = requests.get(stock_url)
'''
#r = requests.head(stock_url)
#print r.headers
'''
data = r.text
soup = BeautifulSoup(data, "html.parser")
'''