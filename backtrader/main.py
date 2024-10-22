import backtrader as bt
from backtrader import cerebro
from diffClacEveryTickStrat import diffClacEveryTickStrat
from diffClacTradeStartStrat import diffClacTradeStartStrat
from staticDiffStrat import staticDiffStrat
from EMACrossoverStrategy import EMACrossoverStrategy
from EMACrossoverStratergyNoStopLoss import EMACrossoverStrategyNoStopLoss
from VWAP_Boll_EMA_Strategy import VWAP_Boll_EMA_Strategy
from EMAtest import EMAtest
from summary import summary
import output

def main():
    runOrder = 1
    strats = [EMAtest]
    fxData = ['test.csv']
    conditions = []
    for o in range(10):
        for i in range(10):
            conditions.append([(o+1)*10, (i+1)*10])
    conditions = [[20, 9]]
    conditions = [0]
    for o in strats:
        for m in fxData:
            for i in conditions:
                cerebro = bt.Cerebro()
                arr = []
                plotData = []
                # cerebro.addstrategy(o, arr=arr, i=i, plotData=plotData)
                cerebro.addstrategy(o)
                data = bt.feeds.MT4CSVData(dataname=m, timeframe=bt.TimeFrame.Minutes, compression=1)
                cerebro.adddata(data)
                cerebro.run()
                # output_text = summary(arr, data)
                # print(plotData)
                # with open("output.txt", "a") as file:
                #     file.write(str(output_text))
                #     file.write('\n')
                #
                # output.createHTMLfile("output.html", str(runOrder)+str(o).replace("<class", "") + " " + str(m) + " " + str(i) + " " + str(output_text),
                #                       output.plotChart())
                # runOrder += 1

if __name__ == "__main__":
    main()
    print("Finished")
    exit(69)