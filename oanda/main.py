import requests
from EMACrossOver import EMACrossOver
import functions
import json
import time

def main():
    list = functions.startPastPricesList()
    x = EMACrossOver(list)

    while True:
        x.tick()  # Execute the EMA crossover strategy
        time.sleep(300)  # Sleep for 5 minutes (300 secs)

if __name__ == "__main__":
    main()
