# types of trades to test:
# win from buy trade from no position 1
# even from buy trade from no position 1
# loss from buy trade from no position 1
# win from sell trade from no position 1
# even from sell trade from no position 1
# loss from sell trade from no position 1
# win buy trade from long position 1
# even buy trade from long position 1
# loss buy trade from long position 1
# win sell trade from short position 1
# even sell trade from short position 1
# loss sell trade from short position
# win buy trade from short position which is equal to the oldest sell trade
# even buy trade from short position which is equal to the oldest sell trade
# loss buy trade from short position which is equal to the oldest sell trade
# win buy trade from short position which is less than the oldest sell trade
# even buy trade from short position which is less than the oldest sell trade
# loss buy trade from short position which is less than the oldest sell trade
# win buy trade from short position which is greater than the oldest sell trade
# even buy trade from short position which is greater than the oldest sell trade
# loss buy trade from short position which is greater than the oldest sell trade
# win sell trade from long position which is equal to the oldest buy trade
# even sell trade from long position which is equal to the oldest buy trade
# loss sell trade from long position which is equal to the oldest buy trade
# win sell trade from long position which is less than the oldest buy trade
# even sell trade from long position which is less than the oldest buy trade
# loss sell trade from long position which is less than the oldest buy trade
# win sell trade from long position which is greater than the oldest buy trade
# even sell trade from long position which is greater than the oldest buy trade
# loss sell trade from long position which is greater than the oldest buy trade
# win buy trade from short position which is equal to the whole short position
# even buy trade from short position which is equal to the whole short position
# loss buy trade from short position which is equal to the whole short position
# win sell trade from long position which is equal to the whole long position
# even sell trade from long position which is equal to the whole long position
# loss sell trade from long position which is equal to the whole long position
# win buy trade from short position which is greater than the whole short position
# even buy trade from short position which is greater than the whole short position
# loss buy trade from short position which is greater than the whole short position
# win sell trade from long position which is greater than the whole long position
# even sell trade from long position which is greater than the whole long position
# loss sell trade from long position which is greater than the whole long position
import json
import csv
def floatCast(o):
    try:
        for key, value in o.items():
            try:
                o[key] = float(value)
            except ValueError:
                pass
            except TypeError:
                floatCast(o[key])
    except AttributeError:
        for i in o:
            floatCast(i)


def summary(time, transactions):
    profit = 0
    openUnits = 0
    openTrades = []
    # print(len(transactions))
    with open('transactions.json', 'w', newline='') as file:
        json.dump(transactions, file, indent=4)
    #convert all values to floats
    for o in transactions:
        floatCast(o)
    # main loop
    for o in transactions:
        # refeshing openUnits
        openUnits = 0
        for i in openTrades:
            openUnits += i['units']
        if o['type'] == "ORDER_FILL":
            # if there are no open trades append the current trade
            if openUnits == 0:
                openTrades.append(o)
            # if there are open buy trades and the current trade is a buy trade append the current trade
            elif openUnits > 0 and o['units'] > 0:
                openTrades.append(o)
            # if there are open sell trades and the current trade is a sell trade append the current trade
            elif openUnits < 0 and o['units'] < 0:
                openTrades.append(o)
            # if there are open buy trades and the current trade is a sell trade
            elif openUnits > 0 and o['units'] < 0:
                # loop though all open trades
                for i in range(len(openTrades)):
                    # the current trades units has been reduced to 0
                    if o['units'] == 0:
                        break
                    # if the current trade is equal to the open trade
                    elif abs(o['units']) == openTrades[i]['units']:
                        profit += (o['price'] - openTrades[i]['price']) * abs(o['units'])
                        openTrades[i]['units'] = 0
                        o['units'] = 0
                        break
                    # if the current trade is greater than the open trade
                    elif abs(o['units']) > openTrades[i]['units']:
                        profit += (o['price'] - openTrades[i]['price']) * openTrades[i]['units']
                        o['units'] += openTrades[i]['units']
                        openTrades[i]['units'] += o['units']
                    # if the current trade is less than the open trade
                    elif abs(o['units']) < openTrades[i]['units']:
                        profit += (o['price'] - openTrades[i]['price']) * abs(o['units'])
                        openTrades[i]['units'] += o['units']
                        o['units'] = 0
                        break

                    try:
                        for i in range(len(openTrades)):
                            if openTrades[i]['units'] == 0:
                                openTrades.pop(i)
                    except IndexError:
                        pass
            # if there are open sell trades and the current trade is a buy trade
            elif openUnits < 0 and o['units'] > 0:
                # loop though all open trades
                for i in range(len(openTrades)):
                    # the current trades units has been reduced to 0
                    if o['units'] == 0:
                        break
                    # if the current trade is equal to the open trade
                    elif o['units'] == abs(openTrades[i]['units']):
                        profit += (openTrades[i]['price'] - o['price']) * o['units']
                        openTrades[i]['units'] = 0
                        o['units'] = 0
                        break
                    # if the current trade is greater than the open trade
                    elif o['units'] > abs(openTrades[i]['units']):
                        profit += (openTrades[i]['price'] - o['price']) * abs(openTrades[i]['units'])
                        o['units'] += openTrades[i]['units']
                        openTrades[i]['units'] += o['units']
                    # if the current trade is less than the open trade
                    elif o['units'] < abs(openTrades[i]['units']):
                        profit += (openTrades[i]['price'] - o['price']) * o['units']
                        openTrades[i]['units'] += o['units']
                        o['units'] = 0
                        break
                try:
                    for i in range(len(openTrades)):
                        if openTrades[i]['units'] == 0:
                            openTrades.pop(i)
                except IndexError:
                    pass

    # x = 0
    # for o in transactions:
    #     pop = 0
    #     copyList = openTrades.copy()
    #     x += 1
    #     if len(openTrades) == 0:
    #         units = 0
    #     for i in range(len(openTrades)):
    #         units += openTrades[i]['units']
    #         if openTrades[i]['units'] == 0:
    #             copyList.pop(i - pop)
    #             pop += 1
    #     openTrades = copyList.copy()
    #     # print("units:", units)
    #     # print("openTrades:", openTrades)
    #     # print("current:", o['units'])
    #     # print("profit:", profit)
    #     if o['type'] == "ORDER_FILL":
    #         if units == 0:
    #             openTrades.append(o)
    #
    #         elif units != 0:
    #             for i in range(len(openTrades)):
    #                 units = sum([i['units'] for i in openTrades])
    #                 if units > 0 and o['units'] > 0:
    #                     openTrades.append(o)
    #                     break
    #
    #                 elif units < 0 and o['units'] < 0:
    #                     openTrades.append(o)
    #                     break
    #
    #                 # long pos sell trade
    #                 elif units > 0 > o['units']:
    #                     if openTrades[i]['units'] == abs(o['units']):
    #                         profit += (o['price'] - openTrades[i]['price']) * abs(openTrades[i]['units'])
    #                         openTrades.pop(i)
    #                         break
    #                     elif openTrades[i]['units'] > abs(o['units']):
    #                         profit += (o['price'] - openTrades[i]['price']) * abs(o['units'])
    #                         openTrades[i]['units'] += o['units']
    #                         break
    #                     elif openTrades[i]['units'] < abs(o['units']):
    #                         profit += (o['price'] - openTrades[i]['price']) * abs(o['units'])
    #                         o['units'] += openTrades[i]['units']
    #                         openTrades[i]['units'] = 0
    #                         # openTrades.pop(i)
    #
    #                 # short pos buy trade
    #                 elif units < 0 < o['units']:
    #                     if abs(openTrades[i]['units']) == o['units']:
    #                         profit += (openTrades[i]['price'] - o['price']) * abs(openTrades[i]['units'])
    #                         openTrades.pop(i)
    #                         break
    #                     elif abs(openTrades[i]['units']) > o['units']:
    #                         profit += (openTrades[i]['price'] - o['price']) * abs(o['units'])
    #                         openTrades[i]['units'] -= o['units']
    #                         break
    #                     elif abs(openTrades[i]['units']) < o['units']:
    #                         profit += (openTrades[i]['price'] - o['price']) * abs(o['units'])
    #                         o['units'] -= openTrades[i]['units']
    #                         openTrades[i]['units'] = 0
    #                         # openTrades.pop(i)

    # print(profit)
    with open('profit1.csv', 'a', newline='') as csvfile:
        csvWriter = csv.writer(csvfile)
        csvWriter.writerow([time, profit])
    csvfile.close()
