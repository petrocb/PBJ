import backtrader as bt
import numpy as np
from strategy import Strategy
#import pandas as pd
#from summary import summary

#for s in range(1, 2):
list = []
    #sp = s / 10000
    #print('sp:',sp)
cerebro = bt.Cerebro()
cerebro.addstrategy(Strategy)
data = bt.feeds.MT4CSVData(dataname='C:/Users/St Potrock/Desktop/EURUSD2.csv',
                               timeframe=bt.TimeFrame.Minutes,
                               compression=1)
cerebro.adddata(data)
cerebro.run()

print(cerebro.broker.getvalue())
#summary()
    #cerebro.plot()
