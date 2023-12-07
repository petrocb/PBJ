
def summary(transactions):
    print(transactions)
    units = 0
    profit = 0
    for i in transactions:
        if i['type'] == 'ORDER_FILL':
            units += float(i['units'])
            if units != 0:
                buyPrice = float(i['fullPrice']['asks'][0]['price'])
                inUnits = float(i['units'])
            elif units == 0:
                sellPrice = float(i['fullPrice']['bids'][0]['price'])
                profit += (buyPrice - sellPrice) * inUnits
    print("profit:", profit)
    import csv
    with open('summaryTransactions.csv', 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=' ',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for i in transactions:
            spamwriter.writerow([i])





    # profit = 0
    # for i in account.getActivity().activity:
    #     try:
    #         profit += float(i.pl)
    #     except TypeError as e:
    #         print(e)
    #
    # print("profit:", profit)
    # data = {
    #     'numObs': 0,
    #     'numTrades': 0,
    #     'pnl': 0,
    #     'winRatio': 0,
    #     'wins': 0,
    #     'losses': 0,
    #     'aveHoldingWindow': 0,
    #     'maxHoldingWindow': 0,
    #     'minHoldingWindow': 0
    # }
    # activity = account.getActivity()
    # for i in act:

    # position = 0
    # for i in activity:
    #     position += float(i.units)
    #     if position != 0:
    #         data['numTrades'] += 1

    # # print("Starting summary")
    # if cond == [40, 50]:
    #     pass
    # # print(arr)
    # data = {
    #     'numObs': 0,
    #     'numTrades': 0,
    #     'pnl': 0,
    #     'winRatio': 0,
    #     'wins': 0,
    #     'losses': 0,
    #     'aveHoldingWindow': 0,
    #     'maxHoldingWindow': 0,
    #     'minHoldingWindow': 0
    # }
    # total = 0
    # winRatio = 0
    # count = 0
    # position = 0
    # spread = 0.0001
    # for i in arr:
    #     count += 1
    #     position += i[1]
    #     price = i[0][1]
    #     try:
    #         if position < 0:
    #             total += ((arr[count][0][1] + spread) - (price - spread)) * position
    #             if ((arr[count][0][1] + spread) - (price - spread)) * position > 0:
    #                 data['wins'] += 1
    #             elif ((arr[count][0][1] + spread) - (price - spread)) * position < 0:
    #                 data['losses'] += 1
    #         elif position > 0:
    #             total += ((arr[count][0][1] - spread) - (price + spread)) * position
    #             if ((arr[count][0][1] - spread) - (price + spread)) * position > 0:
    #                 data['wins'] += 1
    #             elif ((arr[count][0][1] - spread) - (price + spread)) * position < 0:
    #                 data['losses'] -= 0
    #     except IndexError as e:
    #         print(e)
    # data['pnl'] = total
    # data['numTrades'] = len(arr)
    # data['winRatio'] = data['wins'] / (data['wins'] + data['losses'])
    # with open('output.csv', 'a', newline='') as csvfile:
    #     csvWriter = csv.writer(csvfile)
    #     csvWriter.writerow([datetime.utcnow(), data])
    # csvfile.close()
