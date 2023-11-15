import functions
import csv
import time


class SMAFollowTrend:
    def __init__(self):
        self.account = "test"
        self.id = 0
        self.data = functions.startPastPricesList(2, "EUR_USD", "M30", self.account)
        self.direction = 0
        self.position = 0
        self.SMA = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    def tick(self):
        if self.account == "test":
            functions.update(self.account)
        self.data = functions.updatePastPrices2(self.data, 2, "EUR_USD", "M30", self.account)
        self.SMA = [functions.sma(self.data[-8:]), functions.sma(self.data[-16:]), functions.sma(self.data[-32:]),
                    functions.sma(self.data[-64:]), functions.sma(self.data[-128:]), functions.sma(self.data[-256:]),
                    functions.sma(self.data[-512:]), functions.sma(self.data[-1025:]),
                    functions.sma(self.data[-2048:]), functions.sma(self.data[-4096:])]

        # print(self.SMA)
        self.direction = 0
        for i in self.SMA:
            if i < self.data[-1][1]:
                self.direction += 1
            elif i > self.data[-1][1]:
                self.direction -= 1

        # print(self.data[-1][1] - self.SMA[0], self.data[-1][1] - self.SMA[1], self.data[-1][1] - self.SMA[2],
        #       self.data[-1][1] - self.SMA[3], self.data[-1][1] - self.SMA[4], self.data[-1][1] - self.SMA[5],
        #       self.data[-1][1] - self.SMA[6], self.data[-1][1] - self.SMA[7], self.data[-1][1] - self.SMA[8],
        #       self.data[-1][1] - self.SMA[9])

        # print("price:", self.data[-1][1], "direction:", self.direction)
        self.direction *= 500
        self.position = functions.getPositions(self.account)['positions']
        if self.position:
            self.position = float(self.position[0]['long']['units']) + float(self.position[0]['short']['units'])
        else:
            self.position = 0
        # print(self.direction, "    ", self.position)
        if self.position != self.direction:
            functions.order(float(self.direction) - float(self.position), self.account, self.account, 0.001, 0.001, 0)
        with open('response.csv', 'a', newline='') as csvfile:
            csvWriter = csv.writer(csvfile)
            csvWriter.writerow([self.direction, self.position, float(self.direction - float(self.position)), self.SMA])
        csvfile.close()


