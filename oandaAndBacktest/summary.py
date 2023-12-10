def summary(transactions):
    profit = 0
    units = 0
    openTrades = []
    for o in transactions:
        if o['type'] == "ORDER_FILL":
            if units == 0:
                units += float(o['units'])
                openTrades.append(o)
            elif units != 0:
                if units > 0 and float(o['units']) > 0:
                    units += float(o['units'])
                    openTrades.append(o)
                elif units < 0 and float(o['units']) < 0:
                    units += float(o['units'])
                    openTrades.append(o)

                # long pos sell trade
                elif units > 0 > float(o['units']):
                    for i in range(len(openTrades)):
                        if float(openTrades[i]['units']) == abs(float(o['units'])):
                            profit += (float(o['price']) - float(
                                openTrades[i]['price'])) * float(openTrades[0]['units'])
                            openTrades.pop(i)
                            break
                        elif float(openTrades[i]['units']) > abs(float(o['units'])):
                            profit += (float(o['price']) - float(
                                openTrades[i]['price'])) * abs(float(o['units']))
                            openTrades[i]['units'] += str(float(openTrades[i]['units']) - abs(float(o['units'])))
                            break
                        elif float(openTrades[i]['units']) < abs(float(o['units'])):
                            profit += (float(o['price']) - float(
                                openTrades[i]['price'])) * abs(float(o['units']))
                            o['units'] -= str(float(openTrades[i]['units']))
                            openTrades.pop(i)
                # short pos buy trade
                elif units < 0 < float(o['units']):
                    if float(openTrades[0]['units']) == abs(float(o['units'])):
                        profit += (float(o['price']) - float(
                            openTrades[0]['price'])) * float(openTrades[0]['units'])
                        openTrades.pop(0)


    print(profit)