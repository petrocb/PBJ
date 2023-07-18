import backtrader as bt
import numpy as np
from strategy import Strategy
import summary
#import pandas as pd
#from summary import summary

def main():
    #for s in range(1, 2):
    list = []
        #sp = s / 10000
        #print('sp:',sp)
    arr = []
    cerebro = bt.Cerebro()
    cerebro.addstrategy(Strategy, arr=arr)
    data = bt.feeds.MT4CSVData(dataname='EURUSD2.csv',
                                   timeframe=bt.TimeFrame.Minutes, compression=1)
    cerebro.adddata(data)
    cerebro.run()

    #print(cerebro.broker.getvalue())
    print(summary.summary(arr, data))
    #cerebro.plot()

if __name__ == "__main__":
    print("pea head")
    main()