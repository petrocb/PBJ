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


def main():
    runOrder = 1
    strats = [SMACrossOver()]
    fxData = ['EURUSD2.csv']
    conditions = []
    for o in range(10):
        for i in range(10):
            conditions.append([(o + 1) * 10, (i + 1) * 10])
    conditions = [[30, 10]]
    # conditions = [[10, 44], [22, 99]]
    data = []

    # for o in strats:
    for m in fxData:
        for i in conditions:
            o = SMACrossOver()
            with open('EURUSD2.csv', newline='') as csvfile:
                reader = csv.reader(csvfile, delimiter=',', quotechar='|')
                count = 0
                for x in reader:
                    arr = []
                    plotData = []
                    # for x in m:
                    try:
                        o.tick([i[0], i[1]])
                    except IndexError as e:
                        # print(e)
                        pass
                # print(getPositions())
                print(i)
            summary(i, getPositions(), data)
            reset()


if __name__ == "__main__":
    main()
