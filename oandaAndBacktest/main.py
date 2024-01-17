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
    cond = []
    for o in range(50):
        for i in range(50):
            if o != i:
                cond.append([(o + 1) * 100, (i + 1) * 100])
    for i in cond:
        print(i)
        a = SMAFollowTrend("test", i)
        try:
            while True:
                a.tick()
        except IndexError as e:
            with open('transactions.json', 'r') as file:
                data = json.load(file)
            summary(0, data, True, i)
            # print(e)
    # with open('transactions.json', 'r') as file:
    #     data = json.load(file)
    #
    # functions.scrapper(10000, "EUR_USD", "M30")

if __name__ == "__main__":
    main()
