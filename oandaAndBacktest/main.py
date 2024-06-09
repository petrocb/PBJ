# # from colored import Fore
# import os
# import shutil
# import time
# from pathlib import Path
# from summary import summary
# from oandaAndBacktest.strats.SMAFollowTrend import SMAFollowTrend
# import json
# from multiprocessing import Pool, current_process
# import tkinter as tk
# import functions
# from decimal import *
# from oandaAndBacktest.strats.highResLongTrend import highResLongTrend
# from oandaAndBacktest.strats.randomDirection import randomDirection
# from oandaAndBacktest.strats.randomDirection2 import randomDirection2
#
# invCount = 0
#
# def process_condition(condition):
#     global invCount
#     condition.append(invCount)
#     invCount += 1
#     print(condition)
#     # print(condition)
#     # a = SMAFollowTrend("test", condition)
#     a = randomDirection("test", condition[0], condition[1], condition[2])
#     # a = randomDirection2("test", condition[0], condition[1], condition[2])
#     try:
#         while True:
#             a.tick()
#     except IndexError as e:
#         with open('poolArtifacts/'+current_process().name+'transactions.json', 'r') as file:
#             data = json.load(file)
#         # if current_process().name == "SpawnPoolWorker-1":
#         #     pass
#         summary(0, data, True, condition, "")
#
# def main():
#     shutil.rmtree('poolArtifacts')
#     # x= os.path.join('..', 'poolArtifacts')
#     os.mkdir('poolArtifacts')
#     # Path("/oandaAndBacktest").mkdir(parents=True, exist_ok=True)
#     conditions = []
#     count = 0
#     setCount = 0
#     loopCount = 0
#     for o in range(10):
#         for m in range(10):
#             for i in range(10):
#             #     for ii in range(8):
#                     # conditions.append([(o + 1) / 100, (m + 1) / 100, (i + 1) / 100 + 0.04, count, setCount, loopCount])
#                 conditions.append([0.09, 0.02, 0.06, count, setCount, loopCount])
#                 loopCount += 1
#                 count += 1
#             setCount += 1
#             count = 0
#     # conditions = [[0.09, 0.02, 0.06]]
#     # conditions = []
#     # for i in range(8):
#     #     conditions.append([0.1, 0.02, 0.08])
#
#     # Create a pool with the desired number of processes
#     with Pool() as pool:
#     #     # Use the pool to parallelize tasks
#         pool.map(process_condition, conditions)
#     # a = SMAFollowTrend("test", [10, 30])
#     # a = SMAFollowTrend("primary", [10, 30])
#     # a = randomDirection("test", 0.1, 0.02, 0.04)
#     # try:
#     #     while True:
#     #         a.tick()
#     #         # print("tick")
#     #         # time.sleep(60)
#     # except IndexError as e:
#     #     with open('poolArtifacts/'+current_process().name+'transactions.json', 'r') as file:
#     #         data = json.load(file)
#     #     summary(0, data, True, 0, "")
#
#
# if __name__ == "__main__":
#     main()
#     # functions.scrapper(1000, "EUR_USD", "D")
#     # functions.getTransactionsSinceID("primary", 15000)
#


# import os
# import shutil
# import time
# from datetime import datetime
# from summary import summary
# import functions
# import json
# from multiprocessing import Pool, current_process
# from oandaAndBacktest.strats.randomDirection import randomDirection
# from oandaAndBacktest.strats.SMAFollowTrend import SMAFollowTrend
# from oandaAndBacktest.strats.ttytDirection import ttytDirection

# def process_condition(condition):
#     print(condition)
#     # a = randomDirection("test", condition[0], condition[1], condition[2])
#     # a = SMAFollowTrend("test", condition)
#     a = ttytDirection("test", condition[0], condition[1], condition[2])
#     try:
#         while True:
#             a.tick()
#     except IndexError as e:
#         with open('poolArtifacts/'+current_process().name+'transactions.json', 'r') as file:
#             data = json.load(file)
#         summary(0, data, True, condition, "")
#
# def main():
#     shutil.rmtree('poolArtifacts')
#     os.mkdir('poolArtifacts')
#
#     # conditions = []
#     # count = 0
#     # setCount = 0
#     # loopCount = 0
#     # for o in range(10):
#     #     for m in range(10):
#     #         for i in range(10):
#     #         #     for ii in range(8):
#     #                 # conditions.append([(o + 1) / 100, (m + 1) / 100, (i + 1) / 100 + 0.04, count, setCount, loopCount])
#     #             conditions.append([0.09, 0.02, 0.06, count, setCount, loopCount])
#     #             loopCount += 1
#     #             count += 1
#     #         setCount += 1
#     #         count = 0
#     conditions = []
#     count = 0
#     setCount = 0
#
#     # for o in range(6):
#     #     for m in range(6):
#     #         for i in range(6):
#     #             for ii in range(10):
#     #                 conditions.append(
#     #                     [(o + 5) / 10000, (m + 5) / 10000, (i + 5) / 10000, count, setCount])
#     #                 count += 1
#     #             setCount += 1
#     # # print(conditions)
#     for o in range(1000k):
#         conditions.append([0, 0, (o + 5) / 10000, count, setCount])
#         count += 1
#     setCount += 1
#     print(conditions)
#     # for o in range(10):
#     #     for m in range(10):
#     #         for i in range(10):
#     #             if o < m:
#     #                 conditions.append([(o + 1) * 10, (m + 1) * 10, (i + 1)/100])
#     #
#     # for i in range(100):
#     # conditions = [[40, 60, 0.02]]
#     for i in conditions:
#         process_condition(i)
#     # with Pool() as pool:
#     #     pool.map(process_condition, conditions)
#     # a = SMAFollowTrend("SMAFollowTrend", [40, 60, 0.02])
#     # while True:
#     #     if datetime.now().minute == 0:
#     #         a.tick()
#     #         time.sleep(5)
#     # functions.marketOrder(500, "", "primary", 0, 0.0001, 0)
#
from oandaAndBacktest.strats.prevDirection import prevDirection
from oandaAndBacktest.strats.heikienAshi1bar import heikienAshi1bar
from oandaAndBacktest.strats.heikienAshi1bar import heikinAshi
from oandaAndBacktest.strats.heikienAshi1bar import heikinAshi2
from oandaAndBacktest.strats.multiResAshi import multiResAshi

import datetime
import functions
import time


def main():
    x = multiResAshi("multiResAshi")
    while True:
        if functions.time("primary").minute == 1 or functions.time("primary").minute == 16 or functions.time("primary").minute == 31:
            x.tick()
        time.sleep(10)


if __name__ == "__main__":
    main()

