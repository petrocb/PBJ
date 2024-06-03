import datetime
from .. import functions
class prevDirection:
    def __init__(self, account, timeFrame):
        self.account = account
        self.timeFrame = timeFrame
        self.data = functions.startPastPricesList(2, "EUR_USD", self.timeFrame, self.account)

    def tick(self):
        if self.account == "test":
            functions.update()
        self.data = functions.updatePastPrices2(self.data, 2, "EUR_USD", self.timeFrame, self.account)
        position = functions.getPositions(self.account)['positions']
        time = False
        if position:
            position = float(position[0]['long']['units']) + float(position[0]['short']['units'])
        else:
            position = 0

        tradingAllowed = True
        for i in functions.getTransactionsSinceDate("primary", datetime.date.today())['transactions']:
            if functions.oanda2pythonTime(i['time']) > datetime.datetime.utcnow() - datetime.timedelta(minutes=5):
                print(i)
                try:
                    if i['type'] == "ORDER_FILL" and i['tradesClosed']:
                        pass
                except KeyError as e:
                    if str(e) == "'tradesClosed'":
                        tradingAllowed = False
                    else:
                        raise

        if self.timeFrame == "M30":
            if functions.time(self.account).minute == 00 or functions.time(self.account).minute == 30:
                time = True

        elif self.timeFrame == "H1":
            if functions.time(self.account).minute == 00:
                time = True

        elif self.timeFrame == "H4":
            if functions.time(self.account).hour % 4 == 0 and functions.time(self.account).minute == 00:
                time = True

        elif self.timeFrame == "D":
            if functions.time(self.account).hour == 00:
                time = True

        price = round((float(functions.getAsk(self.account)) + float(functions.getBid(self.account))) / 2, 5)

        if time and tradingAllowed and position == 0:
            if price < self.data[0][3]:
                functions.marketOrder(-500, self.account, self.account, self.data[0][1], 0, 0)

            elif price > self.data[0][3]:
                functions.marketOrder(500, self.account, self.account, self.data[0][2], 0, 0)

        elif time and tradingAllowed and position != 0:
            functions.marketOrder(position * -1, self.account, self.account, 0, 0, 0)

        print("\ntime:", functions.time("primary"),
              "\ntimeFrame:", self.timeFrame,
              "\nposition:", position,
              "\nprice:", price,
              "\ntime:", time,
              "\ntradingAllowed:", tradingAllowed
              )
