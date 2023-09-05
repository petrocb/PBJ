import requests
import json
import datetime
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


def startPastPricesList():
    time = datetime.datetime.utcnow() - datetime.timedelta(minutes=1)
    prices = requests.get(f"{getCred()[0]}/v3/accounts/{getCred()[2]}/instruments/EUR_USD/candles",
                          headers={'Authorization': f'Bearer {getCred()[1]}'},
                          params={'granularity': 'M5'})
    prices = prices.json()
    return prices

def updatePastPrices(list):
    time = datetime.datetime.utcnow() - datetime.timedelta(minutes=1)
    prices = requests.get(f"{getCred()[0]}/v3/accounts/{getCred()[2]}/instruments/EUR_USD/candles",
                          headers={'Authorization': f'Bearer {getCred()[1]}'},
                          params={'granularity': 'M5', 'from': list['candles'][-1]['time'] })
    print(datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.000Z'))
    prices = prices.json()
    return list.append(prices)
