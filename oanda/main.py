import datetime
import requests
from EMACrossOver import EMACrossOver
from SMACrossOver import SMACrossOver
from newSMACross import NewSMACross
from followTrend import FollowTrend
from SMAFollowTrend import SMAFollowTrend
import functions
import json
import time
import time
from scraper import scaper
def main():
    a = NewSMACross([30, 10, 0.005, 0.005])
    b = FollowTrend()
    c = SMAFollowTrend()
    while True:
        print("SMACross")
        a.tick()
        print("FollowTrend")
        b.tick()
        print("SMAFollowTrend")
        c.tick()
        time.sleep(60)

if __name__ == "__main__":
    main()
