import backtrader as bt
from backtrader import cerebro
from diffClacEveryTickStrat import diffClacEveryTickStrat
from diffClacTradeStartStrat import diffClacTradeStartStrat
from staticDiffStrat import staticDiffStrat
from EMACrossoverStrategy import EMACrossoverStrategy
from VWAP_Boll_EMA_Strategy import VWAP_Boll_EMA_Strategy
from summary import summary
import output

def main():
    runOrder = 1
    strats = [EMACrossoverStrategy]
    fxData = ['EURUSD2.csv']
    conditions = []
    for o in range(10):
        for i in range(10):
            conditions.append([(o+1)*10, (i+1)*10])
    conditions = [[30, 20]]
    for o in strats:
        for m in fxData:
            for i in conditions:
                cerebro = bt.Cerebro()
                arr = []
                cerebro.addstrategy(o, arr=arr, i=i)
                data = bt.feeds.MT4CSVData(dataname=m, timeframe=bt.TimeFrame.Minutes, compression=1)
                cerebro.adddata(data)
                cerebro.run()
                output_text = summary(arr, data)

                with open("output.txt", "a") as file:
                    file.write(str(output_text))
                    file.write('\n')

                output.createHTMLfile("output.html", str(runOrder)+str(o).replace("<class", "") + " " + str(m) + " " + str(i) + " " + str(output_text),
                                      output.plotChart())
                runOrder += 1

if __name__ == "__main__":
    main()
    print("Finished")
    exit(69)