import csv
import datetime

import numpy as np
import pandas as pd
import requests

from dataHandler import dataHandler

dh = dataHandler()


def update():
    dh.update()
    dh.performanceImprovement()
    dh.checkSLnTP()


def getCred(account):
    if account == 'primary':
        return ["https://api-fxpractice.oanda.com", "2a35930fb4d1eaf4b032d8822367d6ab-2563dd26343f638eb8366e58a0e8718c",
                "101-004-25985927-001"]
    elif account == 'SMAFollowTrendSD':
        return ["https://api-fxpractice.oanda.com", "2a35930fb4d1eaf4b032d8822367d6ab-2563dd26343f638eb8366e58a0e8718c",
                "101-004-25985927-005"]
    elif account == 'followTrend':
        return ["https://api-fxpractice.oanda.com", "2a35930fb4d1eaf4b032d8822367d6ab-2563dd26343f638eb8366e58a0e8718c",
                "101-004-25985927-002"]
    elif account == 'SMAFollowTrend':
        return ["https://api-fxpractice.oanda.com", "2a35930fb4d1eaf4b032d8822367d6ab-2563dd26343f638eb8366e58a0e8718c",
                "101-004-25985927-003"]
    elif account == 'SMACrossOver':
        return ["https://api-fxpractice.oanda.com", "2a35930fb4d1eaf4b032d8822367d6ab-2563dd26343f638eb8366e58a0e8718c",
                "101-004-25985927-004"]
    elif account == 'onceSMAFollowSD':
        return ["https://api-fxpractice.oanda.com", "2a35930fb4d1eaf4b032d8822367d6ab-2563dd26343f638eb8366e58a0e8718c",
                "101-004-25985927-006"]
    elif account == 'followSMAangle':
        return ["https://api-fxpractice.oanda.com", "2a35930fb4d1eaf4b032d8822367d6ab-2563dd26343f638eb8366e58a0e8718c",
                "101-004-25985927-004"]
    # elif account == 'backTest':
    #     return ["http://127.0.0.1:8000/api/", "1", "1"]


def getPrice(instrument, account):
    if account == 'test':
        price = dh.getPrice()
    else:
        price = requests.get(f"{getCred(account)[0]}/v3/accounts/{getCred(account)[2]}/pricing",
                             headers={'Authorization': f'Bearer {getCred(account)[1]}'},
                             params={'instruments': instrument})
        # print(price)
        # print(type(price))
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
    if account == "test":
        data = dh.startPastPriceList(count)
    else:
        data = requests.get(f"{getCred(account)[0]}/v3/accounts/{getCred(account)[2]}/instruments/{instrument}/candles",
                            headers={'Authorization': f'Bearer {getCred(account)[1]}'},
                            params={'granularity': timeFrame, 'count': count})
        responceSave("start", data)
        data = data.json()
    jsonSave("start", data)
    # print(data)
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
    if account == "test":
        x = dh.updatePastPrices2()
    else:
        if data[-1][0] < (datetime.datetime.utcnow() - datetime.timedelta(minutes=30)).replace(
                tzinfo=datetime.timezone.utc):
            x = requests.get(
                f"{getCred(account)[0]}/v3/accounts/{getCred(account)[2]}/instruments/{instrument}/candles",
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
    # else:
    #     # print("failed")
    #     pass
    return data

def order(units, cid, account, sld, tpd, tsld):
    if sld != 0 and tpd != 0 and tsld == 0:
        data = {
            "order": {
                "instrument": "EUR_USD",
                "units": str(units),
                "type": "MARKET",
                "stopLossOnFill": {"distance": sld},
                "tradeClientExtensions": {"tag": cid}
            }
        }
    elif sld == 0 and tpd == 0:
        data = {
            "order": {
                "instrument": "GBP_USD",
                "units": str(units),
                "type": "MARKET",
                "tradeClientExtensions": {"tag": cid}
            }
        }
    elif sld != 0 and tpd != 0 and tsld != 0:
        data = {
            "order": {
                "instrument": "EUR_USD",
                "units": str(units),
                "type": "MARKET",
                "stopLossOnFill": {"distance": sld},
                "tradeClientExtensions": {"tag": cid},
                "trailingStopLossOnFill": {"distance": tsld}
            }
        }
    if account == "test":
        id = dh.order(data)
    else:
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
    if account == "test":
        response = dh.getPositions()
    else:
        response = requests.get(f"{getCred(account)[0]}/v3/accounts/{getCred(account)[2]}/openPositions",
                                headers={'Authorization': f'Bearer {getCred(account)[1]}'})
        responceSave("positions", response)
        response = response.json()
    jsonSave("positions", response)
    return response


def getOrders(account):
    responce = requests.get(f"{getCred(account)[0]}/v3/accounts/{getCred(account)[2]}/orders?state=CLOSED",
                            headers={'Authorization': f'Bearer {getCred(account)[1]}'})
    responceSave("OpenOrders", responce)
    responce = responce.json()
    jsonSave("OpenOrders", responce)
    return responce


# def getTrades(account):
#     responce = requests.get(f"{getCred(account)[0]}/v3/accounts/{getCred(account)[2]}/openTrades",
#                             headers={'Authorization': f'Bearer {getCred(account)[1]}'})
#     responceSave("trades", responce)
#     responce = responce.json()
#     jsonSave("trades", responce)
#     return responce

def getTransactionsSinceID(account, id):
    if account == "test":
        responce = dh.getTransactionsSinceID()
    else:
        responce = requests.get(f"{getCred(account)[0]}/v3/accounts/{getCred(account)[2]}/transactions/sinceid?id={id}",
                                headers={'Authorization': f'Bearer {getCred(account)[1]}'})
        responceSave("transactions", responce)
        responce = responce.json()
    jsonSave("transactions", responce)
    return responce


def getTransactionsSinceDate(account, date):
    responce = requests.get(
        f"{getCred(account)[0]}/v3/accounts/{getCred(account)[2]}/transactions/?from={datetime.date.strftime(date, '%Y-%m-%dT')}",
        headers={'Authorization': f'Bearer {getCred(account)[1]}'})
    responceSave("transactionsDate", responce)
    responce = responce.json()
    jsonSave("transactionsDate", responce)
    try:
        new = responce['pages'][-1]
        responce = requests.get(new, headers={'Authorization': f'Bearer {getCred(account)[1]}'})
        responceSave("transactionsDate", responce)
        responce = responce.json()
        jsonSave("transactionsDate", responce)
    except IndexError:
        pass
    return responce


def getTrades(account):
    if account == "test":
        responce = dh.getTrades()
    else:
        responce = requests.get(f"{getCred(account)[0]}/v3/accounts/{getCred(account)[2]}/trades",
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
    return datetime.datetime.utcnow()


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


def std(data):
    newData = []
    for i in data:
        newData.append(i[1])
    return (np.std(newData)) / 2


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
