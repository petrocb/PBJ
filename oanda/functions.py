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
    # responce("price",price)
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
                        params={'granularity': 'M1', 'count': 30})
    # responce("start", data)
    data = data.json()
    data = data['candles']
    prices = []
    for i in data:
        prices.append([i['time'], i['mid']['o'], i['mid']['h'], i['mid']['l'], i['mid']['c'], 0, 0])
    prices = pd.DataFrame(prices)
    prices.columns = ['Date', 'Open', 'High', 'Low', 'Close', 'Volume', 'OpenInterest']
    list = prices['Close'].to_list()
    count = 0
    for i in list:
        list[count] = [datetime.datetime.fromisoformat(prices['Date'][count]),float(i)]
        count += 1
    return list



def updatePastPrices(data):
    # print(datetime.datetime.utcnow())
    # print(datetime.datetime.utcnow() - datetime.timedelta(minutes=5))
    if data[-1][0] < (datetime.datetime.utcnow() - datetime.timedelta(minutes=1)).replace(tzinfo=datetime.timezone.utc):
        x = requests.get(f"{getCred()[0]}/v3/accounts/{getCred()[2]}/instruments/EUR_USD/candles",
                                     headers={'Authorization': f'Bearer {getCred()[1]}'},
                                     params={'granularity': 'M1', 'count': 1})
        # responce("update", x)
        x = x.json()
        x = x['candles']
        prices = []
        for i in x:
            prices.append([i['time'], i['mid']['o'], i['mid']['h'], i['mid']['l'], i['mid']['c'], 0, 0])
        prices = pd.DataFrame(prices)
        prices.columns = ['Date', 'Open', 'High', 'Low', 'Close', 'Volume', 'OpenInterest']
        list = prices['Close'].to_list()
        count = 0
        for i in list:
            list[count] = [datetime.datetime.fromisoformat(prices['Date'][count]), float(i)]
            data.append(list[count])
            count += 1
        if len(data) > 30:
            data.pop(0)
        # print("passed")
        # print(x)
    else:
        # print("failed")
        pass
    return data

def buy():
        # Place a buy trade
        instrument = "EUR_USD"  # Replace with the instrument you want to trade
        units = 10000  # Replace with the desired number of units
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
        # responce("buy", response)
        id = response.json()
        id = id['orderFillTransaction']['id']
        return id

def sell():
        # Place a sell trade
        instrument = "EUR_USD"  # Replace with the instrument you want to trade
        units = -10000  # Replace with the desired number of units (negative for selling)
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
        # responce("sell", response)
        id = response.json()
        id = id['orderFillTransaction']['id']
        return id

def close(trade_id):
        # Close an existing trade by trade ID
        response = requests.put(f"{getCred()[0]}/v3/accounts/{getCred()[2]}/trades/{trade_id}/close",
                                headers={'Authorization': f'Bearer {getCred()[1]}'})
        responce("close", response)
        return response.json()



# Example usage:



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

def sma(data):
    #list = [i[1] for i in data]
    list = []
    for i in data:
        list.append(i[1])
    return sum(list)/len(list)

def responceSave(loc, res):
    file = open("respnce.txt", "a")
    file.write(datetime.datetime.utcnow(),loc,res,"\n")
    file.close()
