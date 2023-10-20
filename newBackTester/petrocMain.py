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
    conditions = [[40, 80, 0.0005]]
    data = []

    # for o in strats:
    for m in fxData:
        for i in conditions:
            o = SMACrossOver()
            with open('EURUSD1min2023.csv', newline='') as csvfile:
                reader = csv.reader(csvfile, delimiter=',', quotechar='|')
                count = 0
                for x in reader:
                    arr = []
                    plotData = []
                    # for x in m:
                    # try:
                    o.tick(i)
                    # except IndexError as e:
                    #     # print(e)
                    #     pass
                # print(getPositions())
                print(i)
            summary(i, getPositions(), data, i)
            reset()


if __name__ == "__main__":
    main()
