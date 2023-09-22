import pandas as pd
import requests
import json
import datetime
import numpy as np
import backtrader as bt


def getBid():
    return  0


def getAsk():
    return 0


def startPastPricesList():
    return 0



def updatePastPrices(data):
    return []

def buy_trade():
        pass
def sell_trade():
        pass

def close_trade(trade_id):
        pass


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

