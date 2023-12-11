# from colored import Fore
from SimpleSMA import SIMPLESMA
from summary import summary
from SMAFollowTrend import SMAFollowTrend
from testStrat import TestStrat
import functions


def main():
    a = SMAFollowTrend("test")
    # a = SIMPLESMA("test", "buy")
    try:
        while True:
            a.tick()
    except IndexError as e:
        print(e)
    # print(functions.getTransactionsSinceID("SMAFollowTrendSD", 3828))
    # print(functions.order(-500, "SMAFollowTrendSD", "SMAFollowTrendSD", 0, 0, 0))
    # print(functions.getTransactionsSinceID("SMAFollowTrendSD", 3829))

if __name__ == "__main__":
    main()
