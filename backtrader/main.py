import backtrader as bt
import numpy as np
from diffClacEveryTickStrat import diffClacEveryTickStrat
from diffClacTradeStartStrat import diffClacTradeStartStrat
from staticDiffStrat import staticDiffStrat
from EMACrossoverStrategy import EMACrossoverStrategy
import summary
#import pandas as pd
#from summary import summary

def main():
    cerebro = bt.Cerebro()
    strats = [EMACrossoverStrategy]
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
                #print(summary.summary(arr, data))
                #cerebro.plot()
                output_text = summary.summary(arr, data)

                with open("output.txt", "a") as file:
                    file.write(str(output_text))
                    file.write('\n')

if __name__ == "__main__":
    print("pea head")
    print("Starting")
    main()
    print("Finished")
    exit(69)