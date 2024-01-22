import functions
import csv
from random import randint
from datetime import datetime

class DataScrapper():
  def tick(self, instruments, timeFrame):
    x =functions.scrapper(5000, instruments, timeFrame)
    print(type(x))
    print(x)
    # with open(instruments+timeFrame+str(datetime.now()).replace(" ", "").replace(".", "").replace("-", "").replace(":", "")+'.csv', 'w', newline='') as csvfile:
    #   csvWriter = csv.writer(csvfile)
    #   csvWriter.writerow([0])
    # csvfile.close()
