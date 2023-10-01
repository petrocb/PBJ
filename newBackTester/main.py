from EMACrossOver import EMACrossOver
from summary import summary
import numpy as np
from functions import EMA2
from functions import signals
import csv
def main():
    data = [1.0629,1.0627,1.0626,1.0622,1.0620,1.0615,1.0610,1.0605,1.0599,1.0597,1.0592,1.0590,1.0588,1.0580,1.0588,1.0590,1.0597,1.0599,1.0605,1.0610,1.0626]
    df = EMA2(data,8,3)
    df1 = signals(df)
    print(df1)
    # print(signals(df,8))
    # print(np.diff(signals(df,8)))

    #print(signals(EMA2(data,8,3),"sell only"))
    #runOrder = 1
    #strats = [EMACrossOver()]
    #fxData = ['EURUSD2.csv']
    #conditions = [0]
    #data = []
    #for o in strats:
        #for m in fxData:
            #for i in conditions:
                #with open('EURUSD2.csv', newline='') as csvfile:
                    #reader = csv.reader(csvfile, delimiter=',', quotechar='|')
                    #count = 0
                    #for x in reader:
                # arr = []
                # plotData = []
                # for x in m:
                        #try:
                            #o.tick()
                        #except TypeError as e:
                            #print(e)
                #summary(getPositions(), data)


if __name__ == "__main__":
    main()
