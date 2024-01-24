import csv

import functions


class SIMPLESMA:
    def __init__(self, account, bs):
        self.account = account
        self.bs = bs
        self.id = 0
        self.data = functions.startPastPricesList(9, "EUR_USD", "M5", self.account)
        self.direction = 0
        self.position = 0
        self.SMA = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    def tick(self):
        if self.account == "test":
            functions.update()
        self.data = functions.updatePastPrices2(self.data, 20, "EUR_USD", "M5", self.account)
        self.SMA = [functions.sma(self.data[-9:]), functions.sma(self.data[-20:])]

        # print(self.SMA)
        self.direction = 0
        if self.bs == "sell":
            if self.SMA[0] < self.SMA[1]:
                self.direction = -1
            else:
                self.direction = 0
        if self.bs == "buy":
            if self.SMA[0] > self.SMA[1]:
                self.direction = 1
            else:
                self.direction = 0

        # print("SMA", self.SMA)

        print("price:", self.data[-1][1], "direction:", self.direction)
        self.direction *= 500
        self.position = functions.getPositions(self.account)['positions']
        # print(functions.getPositions(self.account))
        if self.position:
            self.position = float(self.position[0]['long']['units']) + float(self.position[0]['short']['units'])
        else:
            self.position = 0
        print(self.direction, "    ", self.position)
        if self.position != self.direction:
            functions.order(float(self.direction) - float(self.position), self.account, self.account, 0, 0, 0)
        with open('../response.csv', 'a', newline='') as csvfile:
            csvWriter = csv.writer(csvfile)
            csvWriter.writerow([self.direction, self.position, float(self.direction - float(self.position)), self.SMA])
        csvfile.close()
