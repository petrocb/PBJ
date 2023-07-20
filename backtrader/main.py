import backtrader as bt
import numpy as np
from diffClacEveryTickStrat import diffClacEveryTickStrat
from diffClacTradeStartStrat import diffClacTradeStartStrat
import summary
#import pandas as pd
#from summary import summary

def main():
    cerebro = bt.Cerebro()
    strats = [diffClacEveryTickStrat, diffClacTradeStartStrat]
    fxData = ['EURUSD2.csv']
    conditions = [0]
    for o in strats:
        for m in conditions:
            for i in fxData:
                arr = []
                cerebro.addstrategy(o, arr=arr)
                print("Loading data")
                data = bt.feeds.MT4CSVData(dataname=i, timeframe=bt.TimeFrame.Minutes, compression=1)
                cerebro.adddata(data)
                print("Loading data finished")
                cerebro.run()

                #print(cerebro.broker.getvalue())
                print(summary.summary(arr, data))
                #cerebro.plot()

if __name__ == "__main__":
    print("pea head")
    print("Starting")
    main()
    print("Finished")