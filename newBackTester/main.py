from EMACrossOver import EMACrossOver
from summary import summary
from functions import getPositions
import csv
def main():
    runOrder = 1
    strats = [EMACrossOver()]
    fxData = ['EURUSD2.csv']
    conditions = [0]
    data = []
    for o in strats:
        for m in fxData:
            for i in conditions:
                with open('EURUSD2.csv', newline='') as csvfile:
                    reader = csv.reader(csvfile, delimiter=',', quotechar='|')
                    count = 0
                    for x in reader:
                # arr = []
                # plotData = []
                # for x in m:
                        try:
                            o.tick()
                        except TypeError as e:
                            print(e)
                summary(getPositions(), data)


if __name__ == "__main__":
    main()
