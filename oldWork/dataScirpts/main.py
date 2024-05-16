import functions
import pandas as pd
import csv
def main():
    data = []
    file = 'EUR_USD_D_2024_04_02T21_00_00_2020_05_27T21_00_00_1000'
    # with open(file+'.csv', 'r') as csvfile:
    #     reader = csv.reader(csvfile)
    #     for row in reader:
    #         data.append(row)
    data = pd.read_csv(file+'.csv', header=None, names=['time', 'open', 'high', 'low', 'close', 'volume', 'direction'])
    data = functions.test(data)
    print(data)
    data.to_csv(file+'processed.csv', index=False, header=True)

    # data = functions.filter(data)
    # data = functions.spread(data)
    # data = functions.upOrDown(data)
    # functions.removeDirection(data)

    # with open(file+'processed.csv', 'w', newline='') as csvfile:
    #     writer = csv.writer(csvfile)
    #     for row in data:
    #         writer.writerow(row)
if __name__ == "__main__":
    main()
