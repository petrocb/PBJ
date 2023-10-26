import functions
import csv
import time


class FollowTrend:
    def __init__(self, cond):
        self.cond = cond
        self.id = 0
        self.data = functions.startPastPricesList(289, "USD_JPY", "M5")
        self.direction = 0
        self.position = 0
        self.closed = True

    def tick(self):
            functions.checkSLnTP()
            self.data = functions.updatePastPrices(self.data, 289, "USD_JPY", "M5")

            time = functions.time()
        # if 6 < time < 23:
            self.closed = False
            self.direction = functions.trend(self.data) * 500
            self.position = functions.openTrades()['positions']
            if self.position:
                self.position = float(self.position[0]['long']['units']) + float(self.position[0]['short']['units'])
                print(self.direction, "    ", self.position)
            else:
                self.position = 0
            if self.position != self.direction:
                print(self.direction, "    ", self.position)
                functions.order(float(self.direction) - float(self.position))
        # elif time > 19 and not self.closed:
        #     self.position = functions.openTrades()['positions']
        #     self.position = self.position['long']['units'] + self.position['short']['units']
        #     if self.position == 0:
        #         self.closed = True
        #
        #     functions.order(0 - self.position)
            with open('response.csv', 'a', newline='') as csvfile:
                csvWriter = csv.writer(csvfile)
                csvWriter.writerow([])
            csvfile.close()
