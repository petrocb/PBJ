import functions
import pandas as pd
import csv
def main():
    data = []
    with open('EURUSD1month2020.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            data.append(row)
    data = functions.filter(data)
    # data = functions.spread(data)
    # data = functions.upOrDown(data)
    # functions.removeDirection(data)

    with open('EURUSD1month2020.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for row in data:
            writer.writerow(row)
if __name__ == "__main__":
    main()
