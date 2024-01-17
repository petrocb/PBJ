import json
import csv
from datetime import datetime
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


def summary(time, transactions, op, cond):
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
        if not openTrades:
            openUnits = 0
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

    with open('profit1.csv', 'a', newline='') as csvfile:
        csvWriter = csv.writer(csvfile)
        csvWriter.writerow([time, profit])
    csvfile.close()

    if op:
        with open('profit.csv', 'a', newline='') as csvfile:
            csvWriter = csv.writer(csvfile)
            csvWriter.writerow([datetime.now(), cond, profit])
        csvfile.close()