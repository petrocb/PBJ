import requests
from EMACrossOver import EMACrossOver
import functions
import json
import time

def main():
    # list = functions.startPastPricesList()
    #print(functions.startPastPricesList())
    #x = EMACrossOver()

    # while True:
        # x.tick()  # Execute the EMA crossover strategy
        # time.sleep(300)  # Sleep for 5 minutes (300 secs)
    data = [10, 12, 15, 18, 20, 22, 25]
    data = [25, 22, 20, 18, 15, 12, 10]
    ema_values = functions.emaCalc(data)
    print(ema_values)
if __name__ == "__main__":
    main()
