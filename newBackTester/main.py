from EMACrossOver import EMACrossOver

def main():
    runOrder = 1
    strats = [EMACrossOver()]
    fxData = ['EURUSD2.csv']
    conditions = [0]
    for o in strats:
        for m in fxData:
            for i in conditions:
                arr = []
                plotData = []
                for x in m:
                    o.tick()

if __name__ == "__main__":
    main()
