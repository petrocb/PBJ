# from colored import Fore
from SimpleSMA import SIMPLESMA
from summary import summary
from SMAFollowTrend import SMAFollowTrend
from testStrat import TestStrat
import functions
import json
import time

def main():
    # a = SMAFollowTrend("test")
    # a = SIMPLESMA("test", "buy")
    # try:
    #     while True:
    #         a.tick()
    # except IndexError as e:
    #     print(e)
    with open("transactions.json", 'r') as f:
        transactions = json.load(f)
    summary(transactions)
    # print(functions.getTransactionsSinceID("SMAFollowTrendSD", 3833))

if __name__ == "__main__":
    main()
