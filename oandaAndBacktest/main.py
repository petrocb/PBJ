# from colored import Fore
from SimpleSMA import SIMPLESMA
from summary import summary
from SMAFollowTrend import SMAFollowTrend
from testStrat import TestStrat
from dataScraper import DataScrapper
import functions
import json
import time
from multiprocessing import Pool, Process, current_process

# def main():
#     cond = []
#     # for o in range(50):
#     #     for i in range(50):
#     #         if o < i:
#     #             cond.append([(o + 1) * 100, (i + 1) * 100])
#     for i in cond:
#         print(i)
#         a = SMAFollowTrend("test", i)
#         try:
#             while True:
#                 a.tick()
#         except IndexError as e:
#             with open('transactions.json', 'r') as file:
#                 data = json.load(file)
#             summary(0, data, True, i)
#             # print(e)
#     # with open('transactions.json', 'r') as file:
#     #     data = json.load(file)
#     #
#     # functions.scrapper(10000, "EUR_USD", "H1")
#
# if __name__ == "__main__":
#     main()

def process_condition(condition):
    print(condition)
    a = SMAFollowTrend("test", condition)
    try:
        while True:
            a.tick()
    except IndexError as e:
        with open('poolArtifacts/'+current_process().name+'transactions.json', 'r') as file:
            data = json.load(file)
        summary(0, data, True, condition, "")

def main():
    conditions = []
    # for o in range(50):
    #     for i in range(50):
    #         if o < i:
    #             conditions.append([(o + 1) * 100, (i + 1) * 100])
    # conditions = [[0, 100]]
    for i in range(100):
        conditions.append([0, (i + 1) * 10])
    conditions = [[0, 1920]]

    # Create a pool with the desired number of processes
    with Pool() as pool:
        # Use the pool to parallelize tasks
        pool.map(process_condition, conditions)

if __name__ == "__main__":
    main()
    # functions.scrapper(100000, "EUR_USD", "M5")