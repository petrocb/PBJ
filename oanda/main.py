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
from SMAFollowTrendStanDiv import SMAFollowTrendStanDiv
def main():
    a = NewSMACross([30, 10, 0.0005, 0.0005])
    b = FollowTrend()
    c = SMAFollowTrend()
    d = SMAFollowTrendStanDiv()
    while True:
        print("SMACross")
        a.tick()
        print("FollowTrend")
        b.tick()
        print("SMAFollowTrend")
        c.tick()
        print("SMAFollowTrendSD")
        d.tick()
        time.sleep(60)




if __name__ == "__main__":
    main()
