# from colored import Fore
import time

from summary import summary
from oandaAndBacktest.strats.SMAFollowTrend import SMAFollowTrend
import json
from multiprocessing import Pool, current_process
import tkinter as tk
import functions
from decimal import *
from oandaAndBacktest.strats.highResLongTrend import highResLongTrend
from oandaAndBacktest.strats.randomDirection import randomDirection

def process_condition(condition):
    print(condition)
    # a = SMAFollowTrend("test", condition)
    a = randomDirection("test", condition[0], condition[1], condition[2])
    try:
        while True:
            a.tick()
    except IndexError as e:
        with open('poolArtifacts/'+current_process().name+'transactions.json', 'r') as file:
            data = json.load(file)
        summary(0, data, True, condition, "")

def main():
    conditions = []
    for o in range(10):
        for m in range(10):
            for i in range(10):
                conditions.append([(o + 1) / 100, (m + 1) / 100, (i + 1) / 100])
    # conditions = [[0.05, 0.05, 0.05]]

    # Create a pool with the desired number of processes
    with Pool() as pool:
        # Use the pool to parallelize tasks
        pool.map(process_condition, conditions)
    # a = SMAFollowTrend("test", [10, 30])
    # a = SMAFollowTrend("primary", [10, 30])
    # a = randomDirection("test", 0.1, 0.02, 0.04)
    # try:
    #     while True:
    #         a.tick()
    #         # print("tick")
    #         # time.sleep(60)
    # except IndexError as e:
    #     with open('poolArtifacts/'+current_process().name+'transactions.json', 'r') as file:
    #         data = json.load(file)
    #     summary(0, data, True, 0, "")


if __name__ == "__main__":
    main()
    # functions.scrapper(1000, "EUR_USD", "H1")
    # functions.getTransactionsSinceID("primary", 15000)