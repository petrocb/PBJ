import datetime

import functions
import csv
import time
import numpy


class oncesMAFollowSD:
    def __init__(self):
        self.id = 0
        self.data = functions.startPastPricesList(4097, "EUR_USD", "M30", "onceSMAFollowSD")
        self.direction = 0
        self.position = 0
        self.SMA = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.sd = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.tradingAllowed = True

    def tick(self):
        functions.checkSLnTP()
        try:
            transactions = functions.getTransactionsSinceDate("onceSMAFollowSD", datetime.date.today())['transactions']
            for i in transactions:

                if i['reason'] == "STOP_LOSS_ORDER" or i['reason'] == "TRAILING_STOP_LOSS_ORDER":
                    self.tradingAllowed = False
        except KeyError:
            pass
        self.data = functions.updatePastPrices2(self.data, 4097, "EUR_USD", "M30", "onceSMAFollowSD")
        self.SMA = [functions.sma(self.data[-8:]), functions.sma(self.data[-16:]), functions.sma(self.data[-32:]),
                    functions.sma(self.data[-64:]), functions.sma(self.data[-128:]), functions.sma(self.data[-256:]),
                    functions.sma(self.data[-512:]), functions.sma(self.data[-1025:]),
                    functions.sma(self.data[-2048:]), functions.sma(self.data[-4096:])]

        self.sd = [functions.std(self.data[-8:]), functions.std(self.data[-16:]), functions.std(self.data[-32:]),
                   functions.std(self.data[-64:]), functions.std(self.data[-128:]), functions.std(self.data[-256:]),
                   functions.std(self.data[-512:]), functions.std(self.data[-1024:]), functions.std(self.data[-2048:]),
                   functions.std(self.data[-4096:])]
        print("sd", self.sd)

        print("SMA2", self.SMA)
        self.direction = 0
        for i in range(len(self.SMA)):
            # print("!!!!!", self.SMA[i] - self.sd[i], self.SMA[i] + self.sd[i], self.SMA[i] - self.sd[i] < self.data[-1][1] < self.SMA[i] + self.sd[i])
            if self.data[-1][1] > self.SMA[i] + self.sd[i]:
                print("long", self.SMA[i] - self.sd[i], self.SMA[i] + self.sd[i],
                      self.SMA[i] - self.sd[i] < self.data[-1][1], self.data[-1][1] < self.SMA[i] + self.sd[i],
                      self.SMA[i] - self.sd[i] < self.data[-1][1] < self.SMA[i] + self.sd[i])
                self.direction += 1
            elif self.data[-1][1] < self.SMA[i] - self.sd[i]:
                print("short", self.SMA[i] - self.sd[i], self.SMA[i] + self.sd[i],
                      self.SMA[i] - self.sd[i] < self.data[-1][1], self.data[-1][1] < self.SMA[i] + self.sd[i],
                      self.SMA[i] - self.sd[i] < self.data[-1][1] < self.SMA[i] + self.sd[i])
                self.direction -= 1
            else:
                print("!!!!!", self.SMA[i] - self.sd[i], self.SMA[i] + self.sd[i],
                      self.SMA[i] - self.sd[i] < self.data[-1][1], self.data[-1][1] < self.SMA[i] + self.sd[i],
                      self.SMA[i] - self.sd[i] < self.data[-1][1] < self.SMA[i] + self.sd[i])

        # for i in self.SMA:
        #     if i < self.data[-1][1]:
        #         self.direction += 1
        #     elif i > self.data[-1][1]:
        #         self.direction -= 1

        print(self.data[-1][1] - self.SMA[0], self.data[-1][1] - self.SMA[1], self.data[-1][1] - self.SMA[2],
              self.data[-1][1] - self.SMA[3], self.data[-1][1] - self.SMA[4], self.data[-1][1] - self.SMA[5],
              self.data[-1][1] - self.SMA[6], self.data[-1][1] - self.SMA[7], self.data[-1][1] - self.SMA[8],
              self.data[-1][1] - self.SMA[9])

        print("price:", self.data[-1][1], "direction:", self.direction)
        self.direction *= 500
        self.position = functions.getPositions("onceSMAFollowSD")['positions']
        if self.position:
            self.position = float(self.position[0]['long']['units']) + float(self.position[0]['short']['units'])
        else:
            self.position = 0
        print(self.direction, "    ", self.position)
        if self.position != self.direction and 17 > functions.time().hour > 8 and self.tradingAllowed:
            functions.order(float(self.direction) - float(self.position), "onceSMAFollowSD",
                            "onceSMAFollowSD", 0.001, 0.001, 0.001)
        with open('response.csv', 'a', newline='') as csvfile:
            csvWriter = csv.writer(csvfile)
            csvWriter.writerow([self.direction, self.position, float(self.direction - float(self.position)), self.SMA])
        csvfile.close()
