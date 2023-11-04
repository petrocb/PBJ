from datetime import datetime
import csv


def summary(cond, arr):
    # print("Starting summary")
    if cond == [40, 50]:
        pass
    # print(arr)
    data = {
        'numObs': 0,
        'numTrades': 0,
        'pnl': 0,
        'winRatio': 0,
        'wins': 0,
        'losses': 0,
        'aveHoldingWindow': 0,
        'maxHoldingWindow': 0,
        'minHoldingWindow': 0
    }
    total = 0
    winRatio = 0
    count = 0
    position = 0
    spread = 0.0001
    for i in arr:
        count += 1
        position += i[1]
        price = i[0][1]
        try:
            if position < 0:
                total += ((arr[count][0][1] + spread) - (price - spread)) * position
            elif position > 0:
                total += ((arr[count][0][1] - spread) - (price + spread)) * position
        # total += (arr[count][0][1] - price) * position
            print("pos:", position)
            print("price:", price)
            print("res:", arr[count][0][1])
            print("diff:", arr[count][0][1] - price, (arr[count][0][1] - price) * position)
            print("total:", total)
        except IndexError as e:
            print(e)
