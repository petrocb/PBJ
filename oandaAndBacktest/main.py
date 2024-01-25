# from colored import Fore
from summary import summary
from oandaAndBacktest.strats.SMAFollowTrend import SMAFollowTrend
import json
from multiprocessing import Pool, current_process
import functions

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
    conditions = [[0, 10000]]

    # Create a pool with the desired number of processes
    with Pool() as pool:
        # Use the pool to parallelize tasks
        pool.map(process_condition, conditions)

if __name__ == "__main__":
    # main()
    # functions.scrapper(100000, "EUR_USD", "S5")
    print(functions.getTransactionsSinceID("primary", 15256))
    print(functions.getPositions("primary"))
    # functions.limitOrder(500, "", "primary",  )
    ask = float(functions.getAsk("primary"))
    bid = float(functions.getBid("primary"))
    print(ask, bid)
    print(ask - bid)
    print(ask -((ask - bid)*2), round(ask + ((ask - bid) * 4), 3), round(ask - ((ask - bid) * 3), 3))
    functions.limitOrder(500, "", "primary", ask - ((ask - bid)*2), round(ask + ((ask - bid) * 4), 3), round(ask - ((ask - bid) * 3), 3))
    print(functions.getTransactionsSinceID("primary", 15256))
