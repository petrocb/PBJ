from functions import getAsk
from functions import getBid
from functions import getPrice
from datetime import datetime
import csv
class scaper():
    def __init__(self):
        pass

    def tick(self):
        with open('data.csv', 'a', newline='') as csvfile:
            csvWriter = csv.writer(csvfile)
            csvWriter.writerow([datetime.utcnow(), getPrice("EUR_USD")])
        csvfile.close()
