from datetime import timedelta
def summary(arr):
    data = {
        'numObs': 0,
        'numTrades': 0,
        'PnL': 10000 - arr[len(arr)-1][3],
        'winRatio': 0,
        'aveHoldingWindow': 0,
        'maxHoldingWindow': 0,
        'minHoldingWindow': 0
    }
    dates = []
    for i in range(len(arr)):

        if i < len(arr) - 1 and (arr[i][0] == 'b' or arr[i][0] == 's') and arr[i][3] < arr[i+1][3]:
            data['winRatio'] += 1
        else:
            data['winRatio'] -= 1
        # numTrades
        if arr[i][0] == 'cb' or arr[i][0] == 'cs':
            data['numTrades'] += 1
            dates.append(int((arr[i][4] - arr[i-1][4]).total_seconds()))
            data['aveHoldingWindow'] = str(round(sum(dates) / len(dates) // 60 // 60)) + ':' + str(round(sum(dates) / len(dates) / 60 % 60)) + ' hours'
            data['minHoldingWindow'] = str(round(min(dates) // 60 // 60)) + ':' + str(round(min(dates) / 60 % 60)) + ' hours'
            data['maxHoldingWindow'] = str(round(max(dates) // 60 // 60)) + ':' + str(round(max(dates) / 60 % 60)) + ' hours'
    print(dates)
    return data