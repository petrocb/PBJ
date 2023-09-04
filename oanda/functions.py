import requests
import json

def getCred():
    return ["https://api-fxpractice.oanda.com", "554a05a67a483b45171693a0ded86b01-7f36009c47bba3095ed7d8cc9901486c",
            "101-004-25985927-001"]


def getPrice():
    price = requests.get(f"{getCred()[0]}/v3/accounts/{getCred()[2]}/pricing",
                         headers={'Authorization': f'Bearer {getCred()[1]}'},
                         params={'instruments': "EUR_USD"})

    price = price.json()
    price = price['prices'][0]
    return price


def getBid():
    return getPrice()['bids'][0]['price']


def getAsk():
    return getPrice()['asks'][0]['price']


def getPastPrices():
    list = []
    prices = requests.get(f"{getCred()[0]}/v3/accounts/{getCred()[2]}/instruments/EUR_USD/candles",
                          headers={'Authorization': f'Bearer {getCred()[1]}'},
                          params={'granularity': 'M5', 'from': '2023-08-20T00:00:00.000Z'})
    prices = prices.json()
    for i in prices['candles']:
        list.append([i['time'], float(i['mid']['c'])])
    return list
