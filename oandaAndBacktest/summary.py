#types of trades:
# buy trade from no position
# sell trade from no position
# buy trade from long position
# sell trade from short position
# buy trade from short position which is equal to the oldest sell trade
# buy trade from short position which is less than the oldest sell trade
# buy trade from short position which is greater than the oldest sell trade
# sell trade from long position which is equal to the oldest buy trade
# sell trade from long position which is less than the oldest buy trade
# sell trade from long position which is greater than the oldest buy trade
# buy trade from short position which is equal to the whole short position
# sell trade from long position which is equal to the whole long position
# buy trade from short position which is greater than the whole short position
# sell trade from long position which is greater than the whole long position


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


def summary(transactions):
    profit = 0
    units = 0
    openTrades = []
    print(len(transactions))
    # with open('transactions.json', 'w', newline='') as file:
    #     json.dump(transactions, file, indent=4)

    for o in transactions:
        floatCast(o)

    for o in transactions:
        if len(openTrades) == 0:
            units = 0
        for i in range(len(openTrades)):
            units += openTrades[i]['units']
            if openTrades[i]['units'] == 0:
                openTrades.pop(i)
        print("units:", units)
        print("openTrades:", openTrades)
        print("current:", o['units'])
        print("profit:", profit)
        if o['type'] == "ORDER_FILL":
            if units == 0:
                openTrades.append(o)

            elif units != 0:
                for i in range(len(openTrades)):
                    units = sum([i['units'] for i in openTrades])
                    if units > 0 and o['units'] > 0:
                        openTrades.append(o)
                        break

                    elif units < 0 and o['units'] < 0:
                        openTrades.append(o)
                        break

                    # long pos sell trade
                    elif units > 0 > o['units']:
                        if openTrades[i]['units'] == abs(o['units']):
                            profit += (o['price'] - openTrades[i]['price']) * abs(openTrades[i]['units'])
                            openTrades.pop(i)
                            break
                        elif openTrades[i]['units'] > abs(o['units']):
                            profit += (o['price'] - openTrades[i]['price']) * abs(o['units'])
                            openTrades[i]['units'] += o['units']
                            break
                        elif openTrades[i]['units'] < abs(o['units']):
                            profit += (o['price'] - openTrades[i]['price']) * abs(o['units'])
                            o['units'] += openTrades[i]['units']
                            openTrades[i]['units'] = 0
                            # openTrades.pop(i)

                    # short pos buy trade
                    elif units < 0 < o['units']:
                        if abs(openTrades[i]['units']) == o['units']:
                            profit += (openTrades[i]['price'] - o['price']) * abs(openTrades[i]['units'])
                            openTrades.pop(i)
                            break
                        elif abs(openTrades[i]['units']) > o['units']:
                            profit += (openTrades[i]['price'] - o['price']) * abs(o['units'])
                            openTrades[i]['units'] -= o['units']
                            break
                        elif abs(openTrades[i]['units']) < o['units']:
                            profit += (openTrades[i]['price'] - o['price']) * abs(o['units'])
                            o['units'] -= openTrades[i]['units']
                            openTrades[i]['units'] = 0
                            # openTrades.pop(i)

    print(profit)
