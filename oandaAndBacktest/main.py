# from colored import Fore
from SimpleSMA import SIMPLESMA
from summary import summary
from SMAFollowTrend import SMAFollowTrend
from testStrat import TestStrat
import functions


def main():
    a = SIMPLESMA("test", "buy")
    try:
        while True:
            a.tick()
    except IndexError as e:
        print(e)
    # print(functions.getPositions("SMAFollowTrendSD"))

if __name__ == "__main__":
    main()
