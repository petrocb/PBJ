def summary(arr):
    data = {
        'numObs': 0,
        'numTrades': 0,
        'PnL': 0,
        'winRatio': 0,
        'aveHoldingWindow': 0,
        'maxHoldingWindow': 0,
        'minHoldingWindow': 0
    }

    for entry in arr:
        # numTrades
        if entry[0] == 'cb' or entry[0] == 'cs':
            data['numTrades'] += 1





    return data