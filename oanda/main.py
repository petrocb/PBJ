import requests
from EMACrossOver import EMACrossOver
import functions
import json
import time
import backtrader
def main():
    print(functions.EMA2([10, 12, 15, 18, 20, 22, 25]))
    print(functions.emaCalc([10, 12, 15, 18, 20, 22, 25]))
    print(functions.EMA2(([1.09206,1.09201,1.09203,1.09199,1.09196,1.09193,1.09196,1.09197,1.09196,1.09181,1.09180,1.09179,1.09176,1.09180,1.09179,1.09179,1.09183,1.09187,1.09186,1.09183,1.09186,1.09177,1.09184,1.09181,1.09181,1.09172,1.09170,1.09171,1.09171,1.09161,])))
    x = EMACrossOver()
    while True:
        x.tick()
  # x.tick()
    # list = functions.startPastPricesList()
    #print(functions.startPastPricesList())
    #x = EMACrossOver()

    # while True:
        # x.tick()  # Execute the EMA crossover strategy
        # time.sleep(300)  # Sleep for 5 minutes (300 secs)
    #data = [10, 12, 15, 18, 20, 22, 25]
    # data = [25, 22, 20, 18, 15, 12, 10]
    #ema_values = functions.emaCalc(data)
    #print(ema_values)

if __name__ == "__main__":
    main()
