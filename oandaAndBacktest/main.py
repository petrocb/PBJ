# from colored import Fore
from SimpleSMA import SIMPLESMA
from summary import summary
from SMAFollowTrend import SMAFollowTrend
from testStrat import TestStrat
from dataScraper import DataScrapper
import functions
import json
import time

def main():
    a = SMAFollowTrend("test")
    # a = SIMPLESMA("test", "buy")
    # a = TestStrat("test")
    try:
        while True:
            a.tick()
    except IndexError as e:
        print(e)
    # with open('transactions.json', 'r') as file:
    #     data = json.load(file)
    #
    # summary(0, data)
    # functions.scrapper(1000, "EUR_USD", "M30")

if __name__ == "__main__":
    main()
