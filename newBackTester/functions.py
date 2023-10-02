import pandas as pd
import requests
import json
import datetime
import numpy as np
import backtrader as bt
import csv
from dataHandler import dataHandler

dh = dataHandler()


def getBid():
    return 0


def getAsk():
    return 0


def startPastPricesList():
    return dh.start()


def updatePastPrices(data):
    return dh.update()


def buy():
    dh.buy()


def sell():
    dh.sell()


def close():
    dh.close()

def getPositions():
    return dh.getPosition()


def EMA2(p, window_LT=200, window_ST=50, signal_type='buy only'):
    alpha_LT = 2 / (window_LT + 1)
    beta_LT = 1 - alpha_LT
    alpha_ST = 2 / (window_ST + 1)
    beta_ST = 1 - alpha_ST

    signals = np.zeros(len(p))
    if len(p) < window_LT:
        return signals

    ema_LT = list(np.zeros(window_LT) + np.nan) + [np.average(p[0:window_LT])]
    for i in np.arange(window_LT + 1, len(p)):
        ema_LT += [(alpha_LT * p[i]) + (ema_LT[i - 1] * beta_LT)]

    for i in np.arange(len(p) - 1):
        if np.isnan(ema_LT[i]):
            continue

    ema_ST = list(np.zeros(window_ST) + np.nan) + [np.average(p[0:window_ST])]
    for i in np.arange(window_ST + 1, len(p)):
        ema_ST += [(alpha_ST * p[i]) + (ema_ST[i - 1] * beta_ST)]

    for i in np.arange(len(p) - 1):
        if np.isnan(ema_ST[i]):
            continue

        #if ema_LT[i] < ema_ST[i] and (signal_type == 'buy only' or signal_type == 'both'):
            #signals[i] = 1
    for i in np.arange(window_LT , len(p)):
        if ema_LT[i] > ema_ST[i] and (signal_type == 'sell only' or signal_type == 'both'):
            signals[i] = 1
    signals[-1] = 0
    d = {'Price': p, 'EMA_ST': ema_ST, 'EMA_LT': ema_LT, 'Signals': signals}

    df = pd.DataFrame(data=d)

    return df



def EMASL(p, window_LT=200, window_ST=50, signal_type='buy only'):
    alpha_LT = 2 / (window_LT + 1)
    beta_LT = 1 - alpha_LT
    alpha_ST = 2 / (window_ST + 1)
    beta_ST = 1 - alpha_ST

    signals = np.zeros(len(p))
    if len(p) < window_LT:
        return signals

    ema_LT = list(np.zeros(window_LT) + np.nan) + [np.average(p[0:window_LT])]
    for i in np.arange(window_LT + 1, len(p)):
        ema_LT += [(alpha_LT * p[i]) + (ema_LT[i - 1] * beta_LT)]

    for i in np.arange(len(p) - 1):
        if np.isnan(ema_LT[i]):
            continue

    ema_ST = list(np.zeros(window_ST) + np.nan) + [np.average(p[0:window_ST])]
    for i in np.arange(window_ST + 1, len(p)):
        ema_ST += [(alpha_ST * p[i]) + (ema_ST[i - 1] * beta_ST)]

    for i in np.arange(len(p) - 1):
        if np.isnan(ema_ST[i]):
            continue

        #if ema_LT[i] < ema_ST[i] and (signal_type == 'buy only' or signal_type == 'both'):
            #signals[i] = 1
    for i in np.arange(window_LT , len(p)):
        if ema_LT[i] > ema_ST[i] and ema_LT[i-1] <= ema_ST[i-1] and (signal_type == 'sell only' or signal_type == 'both'):
            signals[i] = 1
    signals[-1] = 0
    d = {'Price': p, 'EMA_ST': ema_ST, 'EMA_LT': ema_LT, 'Signals': signals}

    df = pd.DataFrame(data=d)

    return df

























def signals(df, window_LT = 8):
    p = df["Price"]
    signals = np.zeros(len(p))
    if len(p) < window_LT:
        return signals
    for i in np.arange(window_LT + 1, len(p)):
       # if df["EMA_LT"][i] < df["EMA_ST"][i] and (signal_type == 'buy only' or signal_type == 'both'):
       #  signals[i] = 1
       if df["EMA_LT"][i] > df["EMA_ST"][i]:
        signals[i] = 1
        df['Signals'] = np.diff(signals)
    return df

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