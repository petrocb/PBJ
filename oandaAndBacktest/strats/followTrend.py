import csv

import functions


class FollowTrend:
    def __init__(self):
        self.account = "followTrend"
        self.id = 0
        self.data = functions.startPastPricesList(1345, "EUR_USD", "M30", self.account)
        self.direction = 0
        self.position = 0
        self.closed = True

    def tick(self):
        functions.checkSLnTP()
        self.data = functions.updatePastPrices2(self.data, 1345, "EUR_USD", "M30", self.account)

        time = functions.time()
        # if 6 < time < 23:
        self.closed = False
        self.direction = functions.trend(self.data) * 500
        self.position = functions.getPositions(self.account)['positions']
        print(self.direction, "    ", self.position)
        if self.position:
            self.position = float(self.position[0]['long']['units']) + float(self.position[0]['short']['units'])

        else:
            self.position = 0
        if self.position != self.direction:
            print(self.direction, "    ", self.position)
            functions.marketOrder(float(self.direction) - float(self.position), "followTrend", self.account, 0.001,
                                  0.001, 0)
        # elif ime > 19 and not self.closed:
        #     self.position = functions.openTrades()['positions']
        #     self.position = self.position['long']['units'] + self.position['short']['units']
        #     if self.position == 0:
        #         self.closed = True
        #
        #     functions.order(0 - self.position)
        with open('../response.csv', 'a', newline='') as csvfile:
            csvWriter = csv.writer(csvfile)
            csvWriter.writerow([self.direction, self.position, float(self.direction - float(self.position)), self.data])
        csvfile.close()
