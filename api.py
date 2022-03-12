import requests
def getapi():
    url = "https://yh-finance.p.rapidapi.com/auto-complete"
    querystring = {"q": input("Enter company "), "region": "US" }
    headers = {
        'x-rapidapi-host': "yh-finance.p.rapidapi.com",
        'x-rapidapi-key': "fe8d60d5eemshf389a807c4b6cb7p1e02ffjsn2091996495cc"
        }
    response = requests.request("GET", url, headers=headers, params=querystring)
    print(response.text)