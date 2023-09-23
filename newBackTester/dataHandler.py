import csv
import datetime


class dataHandler:
    def __init__(self):
        self.line = 0

    def start(self):
        with open('EURUSD2.csv', newline='') as csvfile:
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
        with open('EURUSD2.csv', newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',', quotechar='|')
            self.line += 1
            print(self.line)
            print(reader[self.line])
            return [datetime.datetime.combine(datetime.date(int(self.line[0][0:4]), int(self.line[0][5:7]), int(self.line[0][8:10])),
                             datetime.time(int(self.line[1][0:2])))]
            return reader[[datetime.datetime.combine(datetime.date(int(self.line[0][0:4]), int(self.line[0][5:7]), int(self.line[0][8:10])),
                             datetime.time(int(self.line[1][0:2]), int(self.line[1][3:5]))), float(self.line[-2])]]
