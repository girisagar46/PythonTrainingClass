import json
from urllib.request import urlopen

with urlopen("https://api.coinmarketcap.com/v1/ticker/?limit=10") as response:
	source = response.read().decode('utf-8')
	json_data = json.loads(source)

for crypto in json_data:
	name = crypto.get("name")
	symbol = crypto.get("symbol")
	price = crypto.get("price_usd")
	#print("{0} : {1} = {2}".format(name, symbol, price))
	print(f"{name} : {symbol} = {price}")