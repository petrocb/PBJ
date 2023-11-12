import functions
import csv
import time


class followSMAangle:
    def __init__(self):
        self.id = 0
        self.data = functions.startPastPricesList(25, "EUR_USD", "M30", "followSMAangle")
        self.direction = 0
        self.position = 0
        self.SMA = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    def tick(self):
        functions.checkSLnTP()
        self.data = functions.updatePastPrices2(self.data, 25, "EUR_USD", "H1", "followSMAangle")
        self.SMA = [functions.sma(self.data[-24:]), functions.sma(self.data[-25: -1])]

        print(self.SMA)
        print(self.SMA[0] - self.SMA[1])
        if -0.001 < self.SMA[0] - self.SMA[1] < 0.001:
            self.direction = 0
        elif self.SMA[0] - self.SMA[1] > 0.001:
            self.direction = 500
        elif self.SMA[0] - self.SMA[1] < 0.001:
            self.direction = -500

        # self.direction = 0
        # for i in self.SMA:
        #     if i < self.data[-1][1]:
        #         self.direction += 1
        #     elif i > self.data[-1][1]:
        #         self.direction -= 1

        # print(self.data[-1][1] - self.SMA[0], self.data[-1][1] - self.SMA[1], self.data[-1][1] - self.SMA[2],
        #       self.data[-1][1] - self.SMA[3], self.data[-1][1] - self.SMA[4], self.data[-1][1] - self.SMA[5],
        #       self.data[-1][1] - self.SMA[6], self.data[-1][1] - self.SMA[7], self.data[-1][1] - self.SMA[8],
        #       self.data[-1][1] - self.SMA[9])

        # print("price:", self.data[-1][1], "direction:", self.direction)
        # self.direction *= 500
        self.position = functions.getPositions("followSMAangle")['positions']
        if self.position:
            self.position = float(self.position[0]['long']['units']) + float(self.position[0]['short']['units'])
        else:
            self.position = 0
        print(self.direction, "    ", self.position)
        if self.position != self.direction:
            functions.order(float(self.direction) - float(self.position), "followSMAangle", "followSMAangle", 0.001, 0.001, 0)
        with open('response.csv', 'a', newline='') as csvfile:
            csvWriter = csv.writer(csvfile)
            csvWriter.writerow([self.direction, self.position, float(self.direction - float(self.position)), self.SMA])
        csvfile.close()


