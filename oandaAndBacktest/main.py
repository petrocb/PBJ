# from colored import Fore
from SimpleSMA import SIMPLESMA
from summary import summary
from SMAFollowTrend import SMAFollowTrend
from testStrat import TestStrat
import functions


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
    # a = TestStrat("test")
    # try:
    #     while True:
    #         a.tick()
    # except IndexError as e:
    #     print(e)
    # print(functions.getTransactionsSinceID("primary", 13208))
    # print("trans", functions.getTransactionsSinceID("test", 0))
    # print("trades", functions.getTrades("test"))
    # print("pos", functions.getPositions("test"))
    # print("primary", functions.getPositions("primary"))
    # print("!!!!!!!!!!!!!!!")
    # functions.order(1000, "test", "test", 0, 0, 0)
    # print("trans", functions.getTransactionsSinceID("test", 0))
    # print("trades", functions.getTrades("test"))
    # print("pos", functions.getPositions("test"))
    # print(functions.getTransactionsSinceID("primary", 13205))
    # print(functions.getPositions("SMAFollowTrendSD"))
    # print(functions.order(500, "SMAFollowTrendSD", "SMAFollowTrendSD", 0, 0, 0))
    # print(functions.getTransactionsSinceID("SMAFollowTrendSD", 3807))
    # print(functions.getPositions("SMAFollowTrendSD"))
    # print(functions.order(-1000, "SMAFollowTrendSD", "SMAFollowTrendSD", 0, 0, 0))
    # print(functions.getPositions("SMAFollowTrendSD"))
    # print(functions.getTransactionsSinceID("SMAFollowTrendSD", 3807))
    # print(functions.close(3798, "SMAFollowTrendSD"))
    # print(functions.getTransactionsSinceID("SMAFollowTrendSD", 3807))
    print(functions.getTrades("SMAFollowTrendSD"))

if __name__ == "__main__":
    main()
