import json
import csv
from datetime import datetime
from multiprocessing import current_process
import os
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

def winLoss(profit, winLossArr):
    if profit > 0:
        winLossArr[0] += 1
    elif profit < 0:
        winLossArr[1] += 1
    elif profit == 0:
        winLossArr[2] += 1

def summary(time, transactions, op, cond, dataString):
    totalProfit = 0
    openUnits = 0
    openTrades = []
    winLossArr = [0, 0, 0]

    # print(len(transactions))
    with open('poolArtifacts/'+current_process().name+'transactions.json', 'w', newline='') as file:
        json.dump(transactions, file)
    #convert all values to floats
    for o in transactions:
        floatCast(o)
    # main loop
    for o in transactions:
        if o['type'] == "ORDER_FILL":
            if o['units'] > 0:
                o['price'] = o['price'] + 0.0001
            elif o['units'] < 0:
                o['price'] = o['price'] - 0.0001
            # refeshing openUnits
            openUnits = 0
            for i in openTrades:
                openUnits += i['units']
            if not openTrades:
                openUnits = 0

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
                        profit = (o['price'] - openTrades[i]['price']) * abs(o['units'])
                        totalProfit += profit
                        winLoss(profit, winLossArr)
                        openTrades[i]['units'] = 0
                        o['units'] = 0
                        break
                    # if the current trade is greater than the open trade
                    elif abs(o['units']) > openTrades[i]['units']:
                        profit = (o['price'] - openTrades[i]['price']) * openTrades[i]['units']
                        totalProfit += profit
                        winLoss(profit, winLossArr)
                        o['units'] += openTrades[i]['units']
                        openTrades[i]['units'] += o['units']
                    # if the current trade is less than the open trade
                    elif abs(o['units']) < openTrades[i]['units']:
                        profit = (o['price'] - openTrades[i]['price']) * abs(o['units'])
                        totalProfit += profit
                        winLoss(profit, winLossArr)
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
                        profit = (openTrades[i]['price'] - o['price']) * o['units']
                        totalProfit += profit
                        winLoss(profit, winLossArr)
                        openTrades[i]['units'] = 0
                        o['units'] = 0
                        break
                    # if the current trade is greater than the open trade
                    elif o['units'] > abs(openTrades[i]['units']):
                        profit = (openTrades[i]['price'] - o['price']) * abs(openTrades[i]['units'])
                        totalProfit += profit
                        winLoss(profit, winLossArr)
                        o['units'] += openTrades[i]['units']
                        openTrades[i]['units'] += o['units']
                    # if the current trade is less than the open trade
                    elif o['units'] < abs(openTrades[i]['units']):
                        profit = (openTrades[i]['price'] - o['price']) * o['units']
                        totalProfit += profit
                        winLoss(profit, winLossArr)
                        openTrades[i]['units'] += o['units']
                        o['units'] = 0
                        break
                try:
                    for i in range(len(openTrades)):
                        if openTrades[i]['units'] == 0:
                            openTrades.pop(i)
                except IndexError:
                    pass
        # print(current_process().name)
    with open('poolArtifacts/'+current_process().name + 'profit1.csv', 'a', newline='') as csvfile:
        csvWriter = csv.writer(csvfile)
        csvWriter.writerow([time, totalProfit, dataString])
    csvfile.close()

    if op:
        profitPoints = []
        with open('poolArtifacts/'+current_process().name+'profit1.csv', 'r') as csvfile:
            csvReader = csv.reader(csvfile)
            for i in csvReader:
                profitPoints.append([i[0], i[1]])
                dataString = i[2]

        os.remove(f'poolArtifacts/{current_process().name}profit1.csv')
        os.remove(f'poolArtifacts/{current_process().name}transactions.json')
        with open('outputPages/profit.csv', 'a', newline='') as csvfile:
            csvWriter = csv.writer(csvfile)
            try:
                winPerc = int(round(winLossArr[0]/(winLossArr[0]+winLossArr[1]), 2)*100)
            except ZeroDivisionError:
                winPerc = 0
            # csvWriter.writerow([datetime.now(), cond, dataString, totalProfit, len(transactions), winLossArr, winPerc, profitPoints] + transactions)
            csvWriter.writerow([datetime.now(), current_process().name, cond, dataString, totalProfit, len(transactions), winLossArr, winPerc, profitPoints] + transactions)
        csvfile.close()

