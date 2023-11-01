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
from SMAFollowTrendStanDivCoolOff import SMAFollowTrendStanDivCoolOff
from colorama import Fore
def main():
    a = NewSMACross([30, 10, 0.0005, 0.0005])
    b = FollowTrend()
    c = SMAFollowTrend()
    d = SMAFollowTrendStanDiv()
    e = SMAFollowTrendStanDivCoolOff
    x = datetime.datetime.utcnow()
    while True:
        if datetime.datetime.utcnow() > x + datetime.timedelta(minutes=1):
            x = datetime.datetime.utcnow()
            print(datetime.datetime.utcnow())
            print("SMACross")
            a.tick()
            print("FollowTrend")
            b.tick()
            print("SMAFollowTrend")
            c.tick()
            print("SMAFollowTrendSD")
            d.tick()
            print("SMAFollowTrendSDCoolOff")
            e.tick()
        time.sleep(10)






if __name__ == "__main__":
    main()
