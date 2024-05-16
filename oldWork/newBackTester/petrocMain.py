# from EMACrossOver import EMACrossOver
from summary import summary
# import pandas as pd
# import numpy as np
# from functions import EMA2
# from functions import signals
import csv
from functions import getPositions
from functions import getOrders
from functions import reset
# from SMACrossOver import SMACrossOver
# from SMACrossOverNoStopLoss import SMACrossOverNoStopLoss
# from testStrat import TestStrat
# from newSMACross import NewSMACross
# from newSMACross2 import NewSMACross2
from SMAFollowTrend import SMAFollowTrend
from SMAFollowTrendStanDivCoolOff import SMAFollowTrendStanDivCoolOff

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
    conditions = [[30, 10, 0.001, 0.001]]#
    conditions = [[30, 10, 0.0005, 0.0005], [10, 30, 0.0005, 0.0005]]
    conditions = [[30, 10, 0.001, 0.001]]
    # for o in range(10):
    #     for i in range(10):
    #         conditions.append([30, 10, (o+1)/10000, (i+1)/10000])
    print(conditions)
    data = []

    # for o in strats:
    for m in fxData:
        for i in conditions:
            o = SMAFollowTrend()
            with open('EURUSD30min2020.csv', newline='') as csvfile:
                reader = csv.reader(csvfile, delimiter=',', quotechar='|')
                for x in reader:
                    try:
                        o.tick()
                    except IndexError as e:
                        print(e)
                        break
                # print(i)
            summary(i, getOrders())
            reset()


if __name__ == "__main__":
    main()
