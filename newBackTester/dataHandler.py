import csv
import datetime


class dataHandler:
    def __init__(self):
        self.line = 0
        self.positions = []
        self.data = []

    def start(self, line):
        with open('EURUSD1min2020.csv', newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',', quotechar='|')
            count = 0
            # data = [[datetime.combine(datetime.date(i[0]),datetime.time(i[1])), i[-2]] for i in reader]
            self.line = line
            for i in reader:
                self.data.append([datetime.datetime.combine(datetime.date(int(i[0][0:4]), int(i[0][5:7]), int(i[0][8:10])),
                             datetime.time(int(i[1][0:2]), int(i[1][3:5]))), float(i[-2])])
                count += 1
                # if count == 30:
                #     self.line = 30
                #     break
            return self.data[:line]

    def update(self, count):
        self.line += 1
        return self.data[self.line]
        # with open('EURUSD3.csv', newline='') as csvfile:
            # reader = csv.reader(csvfile, delimiter=',', quotechar='|')
            # self.line += 1
            # count = 0
            # for i in reader:
            #     if count == self.line:
            #         return [datetime.datetime.combine(datetime.date(int(i[0][0:4]), int(i[0][5:7]), int(i[0][8:10])),
            #                                        datetime.time(int(i[1][0:2]), int(i[1][3:5]))), float(i[-2])]
            #         # return data
            #     count += 1
    def buy(self):
        self.positions.append([self.data[self.line], 'b'])
        # with open('EURUSD3.csv', newline='') as csvfile:
        #     reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        #     count = 0
        #     for i in reader:
        #         if count == self.line:
        #             self.positions.append([i, "b"])
        #         count += 1

    def sell(self):
        self.positions.append([self.data[self.line], 's'])
        # with open('EURUSD3.csv', newline='') as csvfile:
        #     reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        #     count = 0
        #     for i in reader:
        #         if count == self.line:
        #             self.positions.append([i, "s"])
        #         count += 1

    def close(self):
        self.positions.append([self.data[self.line], 'c'])
        # with open('EURUSD3.csv', newline='') as csvfile:
        #     reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        #     count = 0
        #     for i in reader:
        #         if count == self.line:
        #             self.positions.append([i, "c"])
        #         count += 1

    def getPosition(self):
        return self.positions

    def setLine(self):
        self.line = 0

    def reset(self):
        self.line = 0
        self.positions = []
        self.data = []
