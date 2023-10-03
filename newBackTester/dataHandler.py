import csv
import datetime


class dataHandler:
    def __init__(self):
        self.line = 0
        self.positions = []

    def start(self):
        with open('EURUSD3.csv', newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',', quotechar='|')
            count = 0
            # data = [[datetime.combine(datetime.date(i[0]),datetime.time(i[1])), i[-2]] for i in reader]
            data = []
            for i in reader:
                data.append([datetime.datetime.combine(datetime.date(int(i[0][0:4]), int(i[0][5:7]), int(i[0][8:10])),
                             datetime.time(int(i[1][0:2]), int(i[1][3:5]))), float(i[-2])])
                count += 1
                if count == 30:
                    self.line = 30
                    break
            return data

    def update(self):
        with open('EURUSD3.csv', newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',', quotechar='|')
            self.line += 1
            count = 0
            for i in reader:
                if count == self.line:
                    return [datetime.datetime.combine(datetime.date(int(i[0][0:4]), int(i[0][5:7]), int(i[0][8:10])),
                                                   datetime.time(int(i[1][0:2]), int(i[1][3:5]))), float(i[-2])]
                    # return data
                count += 1
    def buy(self):
        with open('EURUSD3.csv', newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',', quotechar='|')
            count = 0
            for i in reader:
                if count == self.line:
                    self.positions.append([i, "b"])
                count += 1

    def sell(self):
        with open('EURUSD3.csv', newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',', quotechar='|')
            count = 0
            for i in reader:
                if count == self.line:
                    self.positions.append([i, "s"])
                count += 1

    def close(self):
        with open('EURUSD3.csv', newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',', quotechar='|')
            count = 0
            for i in reader:
                if count == self.line:
                    self.positions.append([i, "c"])
                count += 1

    def getPosition(self):
        return self.positions
