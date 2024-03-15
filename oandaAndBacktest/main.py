# from colored import Fore
import os
import shutil
import time
from pathlib import Path
from summary import summary
from oandaAndBacktest.strats.SMAFollowTrend import SMAFollowTrend
import json
from multiprocessing import Pool, current_process
import tkinter as tk
import functions
from decimal import *
from oandaAndBacktest.strats.highResLongTrend import highResLongTrend
from oandaAndBacktest.strats.randomDirection import randomDirection


invCount = 0

def process_condition(condition):
    global invCount
    condition.append(invCount)
    invCount += 1
    print(invCount/600*100)
    # print(condition)
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
    shutil.rmtree('poolArtifacts')
    # x= os.path.join('..', 'poolArtifacts')
    os.mkdir('poolArtifacts')
    # Path("/oandaAndBacktest").mkdir(parents=True, exist_ok=True)
    conditions = []
    count = 0
    setCount = 0
    loopCount = 0
    for o in range(10):
        for m in range(10):
            for i in range(6):
                for ii in range(8):
                    conditions.append([(o + 1) / 100, (m + 1) / 100, (i + 1) / 100 + 0.04, count, setCount, loopCount])
                    loopCount += 1
                    count += 1
                setCount += 1
                count = 0
    # conditions = []
    # for i in range(8):
    #     conditions.append([0.1, 0.02, 0.08])

    # Create a pool with the desired number of processes
    with Pool() as pool:
    #     # Use the pool to parallelize tasks
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
    # functions.scrapper(1000, "EUR_USD", "D")
    # functions.getTransactionsSinceID("primary", 15000)