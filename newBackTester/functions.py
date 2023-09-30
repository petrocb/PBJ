import pandas as pd
import requests
import json
import datetime
import numpy as np
import backtrader as bt
import csv
from dataHandler import dataHandler

dp = dataHandler()


def getBid():
    return 0


def getAsk():
    return 0


def startPastPricesList():
    return dp.start()


def updatePastPrices(data):
    return dp.update()


def buy():
    dp.buy()


def sell():
    dp.sell()


def close(trade_id):
    dp.close()

def getPositions():
    return dp.getPosition()


def EMA2(p, window_LT=200):
    alpha_LT = 2 / (window_LT + 1)
    beta_LT = 1 - alpha_LT
    data = p
    p = [i[1] for i in data]
    ema_LT = list(np.zeros(window_LT) + np.nan) + [np.average(p[0:window_LT])]
    for i in np.arange(window_LT + 1, len(p)):
        ema_LT += [(alpha_LT * p[i]) + (ema_LT[i - 1] * beta_LT)]

    for i in np.arange(len(p) - 1):
        print(np.isnan(ema_LT[i]))
        if np.isnan(ema_LT[i]):
            continue
        else:
            return ema_LT[i]
    print(ema_LT)
    print(ema_LT[-1])
    return ema_LT[-1]

def ema(data):
    ema = data[-1][1] * (2 / (len(data) + 1))
    data.pop()
    if len(data) > 0:
        ema += ema(data) * (1 - (2 / (len(data) + 1)))
    return ema

def sma(data):
    #list = [i[1] for i in data]
    list = []
    # print(data)
    for i in data:
        # print(i)
        list.append(i[1])
    return sum(list)/len(list)