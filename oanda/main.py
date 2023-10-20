import requests
from EMACrossOver import EMACrossOver
from SMACrossOver import SMACrossOver
import functions
import json
import time
import time
from scraper import scaper
def main():
    x = SMACrossOver()
    # y = scaper()
    while True:
        x.tick([40, 80, 0.0005])
    #     y.tick()
        time.sleep(60)
    # functions.sell(0.0005)
    # functions.getAsk()
    # functions.close(10266)
    # functions.openTrades()

if __name__ == "__main__":
    main()
