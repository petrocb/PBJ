from datetime import timedelta
def summary(arr, data):
    print("Starting summary")
    initial_value = 10000
    data = {
        'numObs': len(data),
        'numTrades': 0,
        'pnl': arr[-1][3] - initial_value,
        'winRatio': 0,
        'wins': 0,
        'losses': 0,
        'aveHoldingWindow': 0,
        'maxHoldingWindow': 0,
        'minHoldingWindow': 0
    }
    dates = []
    if arr[len(arr)-1][0] == ('b' or 's'):
        print(len(arr))
        x = arr[len(arr)-1].pop
        print(x)
        print(len(arr))
    for i in range(len(arr)):

        # if i < len(arr) - 1 and (arr[i][0] == 'b' or arr[i][0] == 's') and arr[i][3] < arr[i+1][3]:
        #     data['winRatio'] += 1
        # else:
        #     data['winRatio'] -= 1
        # numTrades
        if arr[i][0] == 'cb' or arr[i][0] == 'cs':
            data['numTrades'] += 1
            dates.append(int((arr[i][4] - arr[i-1][4]).total_seconds()))
            if arr[i][3] > arr[i-1][3]:
                data['wins'] +=1

            else:
                data['losses'] += 1

    data['winRatio'] = data['wins'] / data['numTrades']
    data['aveHoldingWindow'] = str(round(sum(dates) / len(dates) // 60 // 60)) + ':' + str(
        round(sum(dates) / len(dates) / 60 % 60)) + ' hours'
    data['minHoldingWindow'] = str(round(min(dates) // 60 // 60)) + ':' + str(round(min(dates) / 60 % 60)) + ' hours'
    data['maxHoldingWindow'] = str(round(max(dates) // 60 // 60)) + ':' + str(round(max(dates) / 60 % 60)) + ' hours'


    return data