import csv
from datetime import datetime

from functions import getPrice


class scaper():
    def __init__(self):
        pass

    def tick(self):
        with open('data.csv', 'a', newline='') as csvfile:
            csvWriter = csv.writer(csvfile)
            csvWriter.writerow([datetime.utcnow(), getPrice("EUR_USD")])
        csvfile.close()
