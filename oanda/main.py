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
from onceSMAFollowSD import oncesMAFollowSD
from followSMAangle import followSMAangle
from colored import Fore

def main():
    a = followSMAangle()
    b = FollowTrend()
    c = SMAFollowTrend()
    d = SMAFollowTrendStanDiv()
    e = SMAFollowTrendStanDivCoolOff()
    f = oncesMAFollowSD()
    x = datetime.datetime.utcnow() - datetime.timedelta(minutes=2)
    while True:
        if datetime.datetime.utcnow() > x + datetime.timedelta(minutes=1):
            x = datetime.datetime.utcnow()
            #         print(datetime.datetime.utcnow())
            print(f"{Fore.rgb('100%', '0%', '0%')}followSMAangle")
            a.tick()
            print(f"{Fore.rgb('100%', '100%', '0%')}FollowTrend")
            b.tick()
            print(f"{Fore.rgb('100%', '0%', '100%')}SMAFollowTrend")
            c.tick()
            print(f"{Fore.rgb('0%', '100%', '0%')}SMAFollowTrendSD")
            d.tick()
            print(f"{Fore.rgb('0%', '100%', '100%')}SMAFollowTrendSDCoolOff")
            e.tick()
            print(f"{Fore.rgb('0%', '0%', '100%')}onceFollow")
            f.tick()
        time.sleep(10)


if __name__ == "__main__":
    main()
