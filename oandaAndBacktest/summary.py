def summary(transactions):
    profit = 0
    units = 0
    openTrades = []
    for i in transactions:
        if i['type'] == "ORDER_FILL":
            if units == 0:
                units += float(i['units'])
                openTrades.append(i)
            elif units != 0:
                if units > 0 and float(i['units']) > 0:
                    units += float(i['units'])
                    openTrades.append(i)
                elif units < 0 and float(i['units']) < 0:
                    units += float(i['units'])
                    openTrades.append(i)

                # long pos sell trade
                elif units > 0 > float(i['units']):
                    if float(openTrades[0]['units']) == abs(float(i['units'])):
                        profit += (float(i['price']) - float(
                            openTrades[0]['price'])) * float(openTrades[0]['units'])
                        openTrades.pop(0)
                    elif float(openTrades[0]['units']) > abs(float(i['units'])):
                        profit += (float(i['price']) - float(
                            openTrades[0]['price'])) * abs(float(i['units']))
                        openTrades += str(float(openTrades[0]['units']) - float(i['units']))
                    elif float(openTrades[0]['units']) < abs(float(i['units'])):
                        pass

                # short pos buy trade
                elif units < 0 < float(i['units']):
                    if float(openTrades[0]['units']) == abs(float(i['units'])):
                        profit += (float(i['price']) - float(
                            openTrades[0]['price'])) * float(openTrades[0]['units'])
                        openTrades.pop(0)


    print(profit)