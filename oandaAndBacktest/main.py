import functions
from SMAFollowTrend import SMAFollowTrend
# from colored import Fore
import datetime
import time
from summary import summary
from SimpleSMA import SIMPLESMA
def main():
    # a = followSMAangle()
    # b = FollowTrend()
    # c = SMAFollowTrend()
    # d = SMAFollowTrendStanDiv()
    # e = SMAFollowTrendStanDivCoolOff()
    # f = oncesMAFollowSD()
    # x = functions.time() - datetime.timedelta(minutes=2)
    # while True:
    #     if datetime.datetime.utcnow() > x + datetime.timedelta(minutes=1):
    #         x = functions.time()
            #         print(datetime.datetime.utcnow())
            # print(f"{Fore.rgb('100%', '0%', '0%')}SMACross")
            # a.tick()
            # print(f"{Fore.rgb('100%', '100%', '0%')}FollowTrend")
            # b.tick()
            # print(f"{Fore.rgb('100%', '0%', '100%')}SMAFollowTrend")
            # c.tick()
            # print(f"{Fore.rgb('0%', '100%', '0%')}SMAFollowTrendSD")
            # d.tick()
            # print(f"{Fore.rgb('0%', '100%', '100%')}SMAFollowTrendSDCoolOff")
            # e.tick()
            # print(f"{Fore.rgb('0%', '0%', '100%')}onceFollow")
            # f.tick()
    #     time.sleep(10)
    a = SIMPLESMA("test","buy")
    try:
        while True:
            a.tick()
    except IndexError as e:
        summary([])
    # print(functions.getTransactionsSinceID('primary', 10000))
if __name__ == "__main__":
    main()
