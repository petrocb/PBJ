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
    x = 0
    print(len(transactions))
    for o in transactions:
        floatCast(o)

    for o in transactions:
        print(x)
        x += 1
        if o['type'] == "ORDER_FILL":
            if units == 0:
                units += o['units']
                openTrades.append(o)

            elif units != 0:
                if units > 0 and o['units'] > 0:
                    units += o['units']
                    openTrades.append(o)

                elif units < 0 and o['units'] < 0:
                    units += o['units']
                    openTrades.append(o)

                # long pos sell trade
                elif units > 0 > o['units']:
                    for i in range(len(openTrades)):
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
                    for i in range(len(openTrades)):
                        if openTrades[i]['units'] == abs(o['units']):
                            profit += (o['price'] - openTrades[i]['price']) * abs(openTrades[i]['units'])
                            openTrades.pop(i)
                            break
                        elif openTrades[i]['units'] > abs(o['units']):
                            profit += (o['price'] - openTrades[i]['price']) * abs(o['units'])
                            openTrades[i]['units'] -= o['units']
                            break
                        elif openTrades[i]['units'] < abs(o['units']):
                            profit += (o['price'] - openTrades[i]['price']) * abs(o['units'])
                            o['units'] -= openTrades[i]['units']
                            openTrades[i]['units'] = 0
                            # openTrades.pop(i)

    print(profit)
