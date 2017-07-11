import requests

url = "https://api.bitfinex.com/v1/trades/BTCUSD"

response = requests.request("GET", url)

print(response.text)