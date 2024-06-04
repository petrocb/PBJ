import datetime
from .. import functions
class heikienAshi1bar:
    def __init__(self, account, timeFrame):
        self.account = account
        self.timeFrame = timeFrame
        self.data = functions.startPastPricesList(3, "EUR_USD", self.timeFrame, self.account)

    def tick(self):
        if self.account == "test":
            functions.update()
        self.data = functions.startPastPricesList(3, "EUR_USD", self.timeFrame, self.account)
        position = functions.getPositions(self.account)['positions']
        if position:
            position = float(position[0]['long']['units']) + float(position[0]['short']['units'])
        else:
            position = 0

        open = round(0.5 * (float(self.data[0][1]) + float(self.data[0][4])),5)
        close = round(0.25 * (float(self.data[1][1]) +
                        float(self.data[1][2]) +
                        float(self.data[1][3]) +
                        float(self.data[1][4])), 5)

        if close > open:
            direction = 500
            sl = self.data[1][2]

        elif close < open:
            direction = -500
            sl = self.data[1][2]
        else:
            direction = 0
            sl = 0

        if position != direction:
            functions.marketOrder(direction, self.account, self.account, 0, 0, 0)


        print("\ntime:", functions.time("primary"),
              "\ntimeFrame:", self.timeFrame,
              "\nposition:", position,
              "\ndirection:", direction,
              "\nopen:", open,
              "\nclose:", close,
              "\ndiff:", close - open
              )

