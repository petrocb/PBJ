import pandas as pd
import requests
import json
import datetime
import numpy as np
import csv


def getCred():
    return ["https://api-fxpractice.oanda.com", "554a05a67a483b45171693a0ded86b01-7f36009c47bba3095ed7d8cc9901486c",
            "101-004-25985927-001"]


def getPrice():
    price = requests.get(f"{getCred()[0]}/v3/accounts/{getCred()[2]}/pricing",
                         headers={'Authorization': f'Bearer {getCred()[1]}'},
                         params={'instruments': "EUR_USD"})
    responceSave("price", price)
    price = price.json()
    jsonSave("price", price)
    # price = price['prices'][0]
    # print(price)
    return price


def getBid():
    return getPrice()['prices'][0]['bids'][0]['price']


def getAsk():
    return getPrice()['prices'][0]['asks'][0]['price']


def startPastPricesList(count):
    data = requests.get(f"{getCred()[0]}/v3/accounts/{getCred()[2]}/instruments/EUR_USD/candles",
                        headers={'Authorization': f'Bearer {getCred()[1]}'},
                        params={'granularity': 'M1', 'count': count})
    responceSave("start", data)
    data = data.json()
    jsonSave("start", data)
    data = data['candles']
    prices = []
    for i in data:
        prices.append([i['time'], i['mid']['o'], i['mid']['h'], i['mid']['l'], i['mid']['c'], 0, 0])
    prices = pd.DataFrame(prices)
    prices.columns = ['Date', 'Open', 'High', 'Low', 'Close', 'Volume', 'OpenInterest']
    list = prices['Close'].to_list()
    count = 0
    for i in list:
        list[count] = [datetime.datetime.fromisoformat(prices['Date'][count]), float(i)]
        count += 1
    return list


def updatePastPrices(data, length):
    # print(datetime.datetime.utcnow())
    # print(datetime.datetime.utcnow() - datetime.timedelta(minutes=5))
    if data[-1][0] < (datetime.datetime.utcnow() - datetime.timedelta(minutes=1)).replace(tzinfo=datetime.timezone.utc):
        x = requests.get(f"{getCred()[0]}/v3/accounts/{getCred()[2]}/instruments/EUR_USD/candles",
                         headers={'Authorization': f'Bearer {getCred()[1]}'},
                         params={'granularity': 'M1', 'count': 1})
        responceSave("update", x)
        x = x.json()
        jsonSave("update", x)
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
        if len(data) > length:
            data.pop(0)
        # print("passed")
        # print(x)
    else:
        # print("failed")
        pass
    return data


def buy(sld, tpd):
    # Place a buy trade
    instrument = "EUR_USD"  # Replace with the instrument you want to trade
    units = 10000  # Replace with the desired number of units
    data = {
        "order": {
            "instrument": instrument,
            "units": str(units),  # Convert units to string
            "type": "MARKET",  # You can use other order types if needed
            "stopLossOnFill": {"distance": sld},
            "takeProfitOnFill": {"distance": tpd}
        }
    }
    response = requests.post(f"{getCred()[0]}/v3/accounts/{getCred()[2]}/orders",
                             headers={'Authorization': f'Bearer {getCred()[1]}'},
                             json=data)
    responceSave("buy", response)
    print(response)
    id = response.json()
    print(id)
    jsonSave("buy", id)
    id = id['orderFillTransaction']['id']

    return id


def sell(sld, tpd):
    # Place a sell trade
    instrument = "EUR_USD"  # Replace with the instrument you want to trade
    units = -10000  # Replace with the desired number of units (negative for selling)
    data = {
        "order": {
            "instrument": instrument,
            "units": str(units),  # Convert units to string
            "type": "MARKET",  # You can use other order types if needed
            "stopLossOnFill": {"distance": sld},
            "takeProfitOnFill": {"distance": tpd}

        }
    }
    response = requests.post(f"{getCred()[0]}/v3/accounts/{getCred()[2]}/orders",
                             headers={'Authorization': f'Bearer {getCred()[1]}'},
                             json=data)
    responceSave("sell", response)
    print(response)
    id = response.json()
    print(id)
    jsonSave("sell", id)
    id = id['orderFillTransaction']['id']
    return id


def close(trade_id):
    # Close an existing trade by trade ID
    response = requests.put(f"{getCred()[0]}/v3/accounts/{getCred()[2]}/trades/{trade_id}/close",
                            headers={'Authorization': f'Bearer {getCred()[1]}'})
    responceSave("close", response)
    r = response.json()
    jsonSave("close", response)
    return r

def openTrades():
    response = requests.get(f"{getCred()[0]}/v3/accounts/{getCred()[2]}/openPositions",
                            headers={'Authorization': f'Bearer {getCred()[1]}'})
    responceSave("open", response)
    response = response.json()
    jsonSave("open", response)
    return response

def time():
    return datetime.datetime.utcnow().hour

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
    list = []
    for i in data:
        list.append(i[1])
    return sum(list) / len(list)


def responceSave(loc, res):
    with open('response.csv', 'a', newline='') as csvfile:
        csvWriter = csv.writer(csvfile)
        csvWriter.writerow([datetime.datetime.utcnow(), loc, res])
    csvfile.close()


def jsonSave(loc, res):
    with open('response.csv', 'a', newline='') as csvfile:
        csvWriter = csv.writer(csvfile)
        csvWriter.writerow([datetime.datetime.utcnow(), loc, res])
    csvfile.close()


def checkSLnTP():
    # implements a back testing function. Not needed in live trading but added to stop errors
    pass


