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
                    for x in reader:
                # arr = []
                # plotData = []
                # for x in m:
                        o.tick()
                summary(getPositions(), data)
if __name__ == "__main__":
    main()
