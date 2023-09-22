from datetime import timedelta
def summary(arr, data):
    print("Starting summary")
    print(arr)
    initial_value = 10000  # Replace this with your actual initial account value

    data = {
        'numObs': len(data),
        'numTrades': 0,
        'pnl': 0,
        'winRatio': 0,
        'wins': 0,
        'losses': 0,
        'aveHoldingWindow': 0,
        'maxHoldingWindow': 0,
        'minHoldingWindow': 0
    }
    if len(arr) >= 2:
        data['pnl'] = arr[-2][3] - initial_value
    else:
        data['pnl'] = 0  # If not enough elements in arr, set pnl to 0
    dates = []
    # if arr[len(arr)-1][0] == ('b' or 's'):
    #     x = arr[len(arr)-1].pop
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

    try:
        data['winRatio'] = data['wins'] / data['numTrades']
    except:
        pass
    try:
        data['aveHoldingWindow'] = str(round(sum(dates) / len(dates) // 60 // 60)) + ':' + str(
            round(sum(dates) / len(dates) / 60 % 60)) + ' hours'
    except:
        pass
    try:
        data['minHoldingWindow'] = str(round(min(dates) // 60 // 60)) + ':' + str(round(min(dates) / 60 % 60)) + ' hours'
        data['maxHoldingWindow'] = str(round(max(dates) // 60 // 60)) + ':' + str(round(max(dates) / 60 % 60)) + ' hours'
    except:
        pass

    return data