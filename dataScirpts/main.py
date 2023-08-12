import functions
import csv
def main():
    data = []
    with open('../backtrader/EURUSD2.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            data.append(row)
    data = functions.spread(data)
    data = functions.upOrDown(data)
    print(data)
if __name__ == "__main__":
    main()
