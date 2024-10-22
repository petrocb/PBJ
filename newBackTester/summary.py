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
                if ((arr[count][0][1] + spread) - (price - spread)) * position > 0:
                    data['wins'] += 1
                elif ((arr[count][0][1] + spread) - (price - spread)) * position < 0:
                    data['losses'] += 1
            elif position > 0:
                total += ((arr[count][0][1] - spread) - (price + spread)) * position
                if ((arr[count][0][1] - spread) - (price + spread)) * position > 0:
                    data['wins'] += 1
                elif ((arr[count][0][1] - spread) - (price + spread)) * position < 0:
                    data['losses'] -= 0
        except IndexError as e:
            print(e)
    data['pnl'] = total
    data['numTrades'] = len(arr)
    data['winRatio'] = data['wins'] / (data['wins'] + data['losses'])
    with open('output.csv', 'a', newline='') as csvfile:
        csvWriter = csv.writer(csvfile)
        csvWriter.writerow([datetime.utcnow(), data])
    csvfile.close()
