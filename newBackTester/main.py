from EMACrossOver import EMACrossOver
from summary import summary
from functions import getPositions
def main():
    runOrder = 1
    strats = [EMACrossOver()]
    fxData = ['EURUSD2.csv']
    conditions = [0]
    data = []
    for o in strats:
        for m in fxData:
            for i in conditions:
                arr = []
                plotData = []
                for x in m:
                    o.tick()
                print(getPositions())
                summary(getPositions(), data)
    print(data)
if __name__ == "__main__":
    main()
