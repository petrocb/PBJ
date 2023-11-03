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
    for i in arr:

        print(i)
        # print(i[-1])
        # print(data['pnl'])
        # print(i[0][1])
        # if i[-1] == 's' or i[-1] == 'b':
        #     price = float(i[0][1])
        #     count += 1
        # elif i[-1] == 'c':
        #     data['numTrades'] += 1
        #     if arr[count-1][-1] == 's':
        #         # data['pnl'] -= float(i[0][1]) - price
        #         data['pnl'] += price - float(i[0][1])
        #         if price > float(i[0][1]):
        #             data['wins'] += 1
        #         else:
        #             data['losses'] += 1
        #     elif arr[count-1][-1] == 'b':
        #         data['pnl'] += float(i[0][1]) - price
        #         if price < float(i[0][1]):
        #             data['wins'] += 1
        #         else:
        #             data['losses'] += 1
        #     count += 1

    #     with open('rawdata.csv', 'a', newline='') as csvfile:
    #         csvWriter = csv.writer(csvfile)
    #         csvWriter.writerow([datetime.utcnow(), i])
    #     csvfile.close()
    # try:
    #     data['winRatio'] = data['wins'] / data['numTrades']
    # except ZeroDivisionError:
    #     pass
            # else:
            #     winRatio -= 1

    # try:
    #     winRatio = round(winRatio/(len(arr)/2), 2)
    # except ZeroDivisionError:
    #     pass
    # with open('output.csv', 'a', newline='') as csvfile:
    #     csvWriter = csv.writer(csvfile)
    #     csvWriter.writerow([datetime.utcnow(), conditions, data])
    # csvfile.close()
    # print(total)
    # print(winRatio)
    # initial_value = 10000  # Replace this with your actual initial account value
    #
    # data = {
    #     'numObs': len(data),
    #     'numTrades': 0,
    #     'pnl': 0,
    #     'winRatio': 0,
    #     'wins': 0,
    #     'losses': 0,
    #     'aveHoldingWindow': 0,
    #     'maxHoldingWindow': 0,
    #     'minHoldingWindow': 0
    # }
    # if len(arr) >= 2:
    #     data['pnl'] = arr[-2][3] - initial_value
    # else:
    #     data['pnl'] = 0  # If not enough elements in arr, set pnl to 0
    # dates = []
    # # if arr[len(arr)-1][0] == ('b' or 's'):
    # #     x = arr[len(arr)-1].pop
    # for i in range(len(arr)):
    #
    #     # if i < len(arr) - 1 and (arr[i][0] == 'b' or arr[i][0] == 's') and arr[i][3] < arr[i+1][3]:
    #     #     data['winRatio'] += 1
    #     # else:
    #     #     data['winRatio'] -= 1
    #     # numTrades
    #     if arr[i][0] == 'cb' or arr[i][0] == 'cs':
    #         data['numTrades'] += 1
    #         dates.append(int((arr[i][4] - arr[i-1][4]).total_seconds()))
    #         if arr[i][3] > arr[i-1][3]:
    #             data['wins'] +=1
    #
    #         else:
    #             data['losses'] += 1
    #
    # try:
    #     data['winRatio'] = data['wins'] / data['numTrades']
    # except:
    #     pass
    # try:
    #     data['aveHoldingWindow'] = str(round(sum(dates) / len(dates) // 60 // 60)) + ':' + str(
    #         round(sum(dates) / len(dates) / 60 % 60)) + ' hours'
    # except:
    #     pass
    # try:
    #     data['minHoldingWindow'] = str(round(min(dates) // 60 // 60)) + ':' + str(round(min(dates) / 60 % 60)) + ' hours'
    #     data['maxHoldingWindow'] = str(round(max(dates) // 60 // 60)) + ':' + str(round(max(dates) / 60 % 60)) + ' hours'
    # except:
    #     pass
    #
    # return data