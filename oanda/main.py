import datetime

import requests
from EMACrossOver import EMACrossOver
from SMACrossOver import SMACrossOver
from newSMACross import NewSMACross
from followTrend import FollowTrend
import functions
import json
import time
import time
from scraper import scaper
def main():
    # x = NewSMACross([30, 10, 0.001, 0.001])
    # y = scaper()
    # while True:
    #     x.tick()
    #     y.tick()
    #     time.sleep(60)#
    # print(functions.openTrades())
    x = FollowTrend([])
    while True:
        x.tick()
        time.sleep(120)



if __name__ == "__main__":
    main()
