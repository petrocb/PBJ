import pandas as pd
import requests
import json
import datetime
import numpy as np
import backtrader as bt
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
    data = requests.get(f"{getCred()[0]}/v3/accounts/{getCred()[2]}/instruments/EUR_USD/candles",
                        headers={'Authorization': f'Bearer {getCred()[1]}'},
                        params={'granularity': 'M5', 'count': 30})
    data = data.json()
    data = data['candles']
    prices = []
    for i in data:
        prices.append([i['time'], i['mid']['o'], i['mid']['h'], i['mid']['l'], i['mid']['c'], 0, 0])
    prices = pd.DataFrame(prices)
    prices.columns = ['Date', 'Open', 'High', 'Low', 'Close', 'Volume', 'OpenInterest']
    list = prices['Close'].to_list()
    print(list)
    count = 0
    for i in list:
        list[count] = [datetime.datetime.fromisoformat(prices['Date'][count]),float(i)]
        count += 1
    print(list)
    return list



def updatePastPrices(data):
    print(datetime.datetime.utcnow())
    print(datetime.datetime.utcnow() - datetime.timedelta(minutes=5))
    if data[-1][0] < datetime.datetime.utcnow() - datetime.timedelta(minutes=5):
        data.append([requests.get(f"{getCred()[0]}/v3/accounts/{getCred()[2]}/instruments/EUR_USD/candles",
                                     headers={'Authorization': f'Bearer {getCred()[1]}'},
                                     params={'granularity': 'M5', 'count': 1})])

    return data

def buy_trade():
        # Place a buy trade
        instrument = "EUR:USD"  # Replace with the instrument you want to trade
        units = 100  # Replace with the desired number of units
        data = {
            "order": {
                "instrument": instrument,
                "units": str(units),  # Convert units to string
                "type": "MARKET"  # You can use other order types if needed
            }
        }
        response = requests.post(f"{getCred()[0]}/v3/accounts/{getCred()[2]}/orders",
                                 headers={'Authorization': f'Bearer {getCred()[1]}'},
                                 json=data)
        return response.json()

def sell_trade():
        # Place a sell trade
        instrument = "EUR:USD"  # Replace with the instrument you want to trade
        units = -100  # Replace with the desired number of units (negative for selling)
        data = {
            "order": {
                "instrument": instrument,
                "units": str(units),  # Convert units to string
                "type": "MARKET"  # You can use other order types if needed
            }
        }
        response = requests.post(f"{getCred()[0]}/v3/accounts/{getCred()[2]}/orders",
                                 headers={'Authorization': f'Bearer {getCred()[1]}'},
                                 json=data)
        return response.json()

def close_trade(trade_id):
        # Close an existing trade by trade ID
        response = requests.put(f"{getCred()[0]}/v3/accounts/{getCred()[2]}/trades/{trade_id}/close",
                                headers={'Authorization': f'Bearer {getCred()[1]}'})
        return response.json()



# Example usage:

def buy(self):
        # Place a buy order
        # You want this to be done a certain way and im not sure of the code
        # Need to define how to tell API to initiate trade in the way you want
        pass

def sell(self):
    # Place a sell order
    # You want this to be done a certain way and im not sure of the code
    # Need to define how to tell API to initiate trade in the way you want
    pass
def close(self):
    # Close an existing order
    # You want this to be done a certain way and im not sure of the code
    # Need to define how to tell API to initiate trade in the way you want
    pass

def EMA2(p, window_LT=200):
    alpha_LT = 2 / (window_LT + 1)
    beta_LT = 1 - alpha_LT
    ema_LT = list(np.zeros(window_LT) + np.nan) + [np.average(p[0:window_LT])]
    for i in np.arange(window_LT + 1, len(p)):
        ema_LT += [(alpha_LT * p[i]) + (ema_LT[i - 1] * beta_LT)]

    for i in np.arange(len(p) - 1):
        if np.isnan(ema_LT[i]):
            continue

    return ema_LT

