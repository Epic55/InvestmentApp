import requests, json
API_TOKEN = 'CSG2DIMZQ74IW1O1'
def getapi():
    symbol1 = input("Enter Ticker ")
    api_url1 = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=' + symbol1 + '&apikey={API_TOKEN}'
    data1 = requests.get(api_url1).json()
    price = data1["Global Quote"]
    if price['05. price'] >= price['08. previous close']:
        char = '+'
    else:
        char = '-'
    print("Ticker - " + price['01. symbol'], ", Price - " + price['05. price'],
          ", Previous price - " + price['08. previous close'], ", Change - " + char + price['10. change percent'])
