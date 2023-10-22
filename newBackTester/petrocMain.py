from EMACrossOver import EMACrossOver
from summary import summary
import pandas as pd
import numpy as np
from functions import EMA2
from functions import signals
import csv
from functions import getPositions
from functions import reset
from SMACrossOver import SMACrossOver
from SMACrossOverNoStopLoss import SMACrossOverNoStopLoss
from testStrat import TestStrat
from newSMACross import NewSMACross

def main():
    runOrder = 1
    # strats = [SMACrossOver()]
    fxData = ['EURUSD.csv']
    conditions = []
    # for o in range(10):
    #     for m in range(10):
    #         for i in range(100):
    #             conditions.append([(o + 1) * 10, (m + 1) * 10, (i + 1) / 10000])

    # for i in range(1000):
    #     conditions.append([30, 10, (i+1)/10000])
    # conditions = [[30, 10], [10, 30]]
    # print(conditions)
    # conditions = [[10, 44], [22, 99]]
    conditions = [[30, 10, 0.0005, 0.0005]]
    data = []

    # for o in strats:
    for m in fxData:
        for i in conditions:
            o = NewSMACross(i)
            with open('EURUSD1min2023.05.csv', newline='') as csvfile:
                reader = csv.reader(csvfile, delimiter=',', quotechar='|')
                for x in reader:
                    try:
                        o.tick()
                    except IndexError as e:
                        print(e)
                        break
                print(i)
            summary(i, getPositions(), data, i)
            reset()


if __name__ == "__main__":
    main()
