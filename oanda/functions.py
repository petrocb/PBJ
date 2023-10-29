import pandas as pd
import requests
import json
import numpy as np
import csv
import datetime

def getCred(account):
    if account == 'followTrend':
        return ["https://api-fxpractice.oanda.com", "f4269a9c72d371dc9004bbea2244baff-bce94bf762cbb36a0d09f0ddc0fcf310",
                "101-004-25985927-002"]
    elif account == 'SMAFollowTrend':
        return ["https://api-fxpractice.oanda.com", "f4269a9c72d371dc9004bbea2244baff-bce94bf762cbb36a0d09f0ddc0fcf310",
                "101-004-25985927-003"]
    elif account == 'SMACrossOver':
        return ["https://api-fxpractice.oanda.com", "f4269a9c72d371dc9004bbea2244baff-bce94bf762cbb36a0d09f0ddc0fcf310",
                "101-004-25985927-004"]



def getPrice(instrument, account):
    price = requests.get(f"{getCred(account)[0]}/v3/accounts/{getCred(account)[2]}/pricing",
                         headers={'Authorization': f'Bearer {getCred(account)[1]}'},
                         params={'instruments': instrument})
    responceSave("price", price)
    price = price.json()
    jsonSave("price", price)
    # price = price['prices'][0]
    # print(price)
    return price


def getPriceSince(instrument, date, account):
    price = requests.get(f"{getCred(account)[0]}/v3/accounts/{getCred(account)[2]}/pricing",
                         headers={'Authorization': f'Bearer {getCred(account)[1]}'},
                         params={'instruments': instrument,
                                 'since': date})
    responceSave("price", price)
    price = price.json()
    jsonSave("price", price)
    # price = price['prices'][0]
    # print(price)
    return price


def getBid(account):
    return getPrice("EUR_USD", account)['prices'][0]['bids'][0]['price']


def getAsk(account):
    return getPrice("EUR_USD", account)['prices'][0]['asks'][0]['price']


def startPastPricesList(count, instrument, timeFrame, account):
    data = requests.get(f"{getCred(account)[0]}/v3/accounts/{getCred(account)[2]}/instruments/{instrument}/candles",
                        headers={'Authorization': f'Bearer {getCred(account)[1]}'},
                        params={'granularity': timeFrame, 'count': count})
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


def updatePastPrices(data, length, instrument, timeFrame, account):
    # print(datetime.datetime.utcnow())
    # print(datetime.datetime.utcnow() - datetime.timedelta(minutes=5))
    if data[-1][0] < (datetime.datetime.utcnow() - datetime.timedelta(minutes=1)).replace(tzinfo=datetime.timezone.utc):
        x = requests.get(f"{getCred(account)[0]}/v3/accounts/{getCred(account)[2]}/instruments/{instrument}/candles",
                         headers={'Authorization': f'Bearer {getCred(account)[1]}'},
                         params={'granularity': timeFrame, 'count': 1})
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


def updatePastPrices2(data, length, instrument, timeFrame, account):
    # print(datetime.datetime.utcnow())
    # print(datetime.datetime.utcnow() - datetime.timedelta(minutes=5))
    if data[-1][0] < (datetime.datetime.utcnow() - datetime.timedelta(minutes=30)).replace(
            tzinfo=datetime.timezone.utc):
        x = requests.get(f"{getCred(account)[0]}/v3/accounts/{getCred(account)[2]}/instruments/{instrument}/candles",
                         headers={'Authorization': f'Bearer {getCred(account)[1]}'},
                         params={'granularity': timeFrame, 'count': 1})
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


def buy(sld, tpd, instrument, cid, account):
    # Place a buy trade
    instrument = instrument  # Replace with the instrument you want to trade
    units = 1000  # Replace with the desired number of units
    if sld != 0 and tpd != 0:
        data = {
            "order": {
                "instrument": instrument,
                "units": str(units),
                "type": "MARKET",
                "stopLossOnFill": {"distance": sld},
                "takeProfitOnFill": {"distance": tpd},
                "tradeClientExtensions": {"tag": cid}
            }
        }
    elif sld == 0 and tpd == 0:
        data = {
            "order": {
                "instrument": instrument,
                "units": str(units),
                "type": "MARKET",
                "tradeClientExtensions": {"tag": cid}
            }
        }
    response = requests.post(f"{getCred(account)[0]}/v3/accounts/{getCred(account)[2]}/orders",
                             headers={'Authorization': f'Bearer {getCred(account)[1]}'},
                             json=data)
    responceSave("buy", response)
    id = response.json()
    jsonSave("buy", id)
    id = id['orderFillTransaction']['id']

    return id


def sell(sld, tpd, instrument, cid, account):
    # Place a sell trade
    instrument = instrument  # Replace with the instrument you want to trade
    units = -1000  # Replace with the desired number of units (negative for selling)
    if sld != 0 and tpd != 0:
        data = {
            "order": {
                "instrument": instrument,
                "units": str(units),
                "type": "MARKET",
                "stopLossOnFill": {"distance": sld},
                "takeProfitOnFill": {"distance": tpd},
                "tradeClientExtensions": {"tag": cid}
            }
        }
    elif sld == 0 and tpd == 0:
        data = {
            "order": {
                "instrument": instrument,
                "units": str(units),
                "type": "MARKET",
                "tradeClientExtensions": {"tag": cid}
            }
        }
    response = requests.post(f"{getCred(account)[0]}/v3/accounts/{getCred(account)[2]}/orders",
                             headers={'Authorization': f'Bearer {getCred(account)[1]}'},
                             json=data)
    responceSave("sell", response)
    id = response.json()
    jsonSave("sell", id)
    id = id['orderFillTransaction']['id']
    return id


def order(units, cid, account, sld, tpd):
    if sld != 0 and tpd != 0:
        data = {
            "order": {
                "instrument": "EUR_USD",
                "units": str(units),
                "type": "MARKET",
                "stopLossOnFill": {"distance": sld},
                "takeProfitOnFill": {"distance": tpd},
                "tradeClientExtensions": {"tag": cid}
            }
        }
    elif sld == 0 and tpd == 0:
        data = {
            "order": {
                "instrument": "EUR_USD",
                "units": str(units),
                "type": "MARKET",
                "tradeClientExtensions": {"tag": cid}
            }
        }
    response = requests.post(f"{getCred(account)[0]}/v3/accounts/{getCred(account)[2]}/orders",
                             headers={'Authorization': f'Bearer {getCred(account)[1]}'},
                             json=data)
    responceSave("order", response)
    id = response.json()
    jsonSave("order", id)
    # id = id['orderFillTransaction']['id']
    # return id


def close(trade_id, account):
    # Close an existing trade by trade ID
    response = requests.put(f"{getCred(account)[0]}/v3/accounts/{getCred(account)[2]}/trades/{trade_id}/close",
                            headers={'Authorization': f'Bearer {getCred(account)[1]}'})
    responceSave("close", response)
    r = response.json()
    jsonSave("close", response)
    return r


def getPositions(account):
    response = requests.get(f"{getCred(account)[0]}/v3/accounts/{getCred(account)[2]}/openPositions",
                            headers={'Authorization': f'Bearer {getCred(account)[1]}'})
    responceSave("positions", response)
    response = response.json()
    jsonSave("positions", response)
    return response

def getOrders(account):
    responce = requests.get(f"{getCred(account)[0]}/v3/accounts/{getCred(account)[2]}/orders",
                            headers={'Authorization': f'Bearer {getCred(account)[1]}'})
    responceSave("OpenOrders", responce)
    responce = responce.json()
    jsonSave("OpenOrders", responce)
    return responce

def getTrades(account):
    responce = requests.get(f"{getCred(account)[0]}/v3/accounts/{getCred(account)[2]}/openTrades",
                            headers={'Authorization': f'Bearer {getCred(account)[1]}'})
    responceSave("trades", responce)
    responce = responce.json()
    jsonSave("trades", responce)
    return responce

def getDirection(list):
    # list = startPastPricesList(60)
    if list[0][1] > list[-1][1]:
        return "down"
    else:
        return "up"


def trend(data):
    total = 0
    # month
    print("month", data[0], data[-1], data[-1][1] - data[0][1])
    if data[0][1] > data[-1][1]:
        total -= 1
    else:
        total += 1

    # week
    print("week", data[1140], data[-1], data[-1][1] - data[1140][1])
    if data[1140][1] > data[-1][1]:
        total -= 1
    else:
        total += 1

    # day
    print("day", data[1296], data[-1], data[-1][1] - data[1296][1])
    if data[1296][1] > data[-1][1]:
        total -= 1
    else:
        total += 1

    # 4 hour
    print("4 hour", data[1336], data[-1], data[-1][1] - data[1336][1])
    if data[1336][1] > data[-1][1]:
        total -= 1
    else:
        total += 1

    # 1 hour
    print("1 hour", data[1342], data[-1], data[-1][1] - data[1342][1])
    if data[1342][1] > data[-1][1]:
        total -= 1
    else:
        total += 1

    # 30 min
    print("30 min", data[1343], data[-1], data[-1][1] - data[1343][1])
    if data[1343][1] > data[-1][1]:
        total -= 1
    else:
        total += 1

    # # 15 min
    # print("15 min", data[285], data[-1], data[-1][1] - data[285][1])
    # if data[285][1] > data[-1][1]:
    #     total -= 1
    # else:
    #     total += 1
    #
    # # 5 min
    # print("5 min", data[287], data[-1], data[-1][1] - data[287][1])
    # if data[287][1] > data[-1][1]:
    #     total -= 1
    # else:
    #     total += 1

    return total

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
    # print(len(list))
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


def generate_timestamp(year, month, day, hour, minute, second):
    timestamp = datetime.datetime(year, month, day, hour, minute, second)
    formatted_timestamp = timestamp.strftime("%Y-%m-%dT%H:%M:%S.%fZ")
    print(formatted_timestamp)
    return formatted_timestamp


def checkSLnTP():
    # implements a back testing function. Not needed in live trading but added to stop errors
    pass
