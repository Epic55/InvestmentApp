import requests
import json
from secrets import IEX_CLOUD_API_TOKEN
def getapi():
    symbol=input("Enter Ticker ")
    api_url = f'https://sandbox.iexapis.com/stable/stock/{symbol}/quote?token={IEX_CLOUD_API_TOKEN}'
    data = requests.get(api_url).json()
    price = data["latestPrice"]
    marketcap = data['marketCap']
    x = "{:.2f}".format(marketcap/1000000000000)
    print("Ticker - ", symbol,", LatestPrice - ",price,"$, Capitalization - ", x,"T")
#test