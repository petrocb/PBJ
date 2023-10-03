import functions
import csv

class SMACrossOver():
  def tick(self):

  with open('output.csv', 'a', newline='') as csvfile:
    csvWriter = csv.writer(csvfile)
    csvWriter.writerow([self.closes, self.short_ema, self.long_ema, self.sellOpen])
  csvfile.close()
