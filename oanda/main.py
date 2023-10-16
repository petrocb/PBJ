import requests
from EMACrossOver import EMACrossOver
from SMACrossOver import SMACrossOver
import functions
import json
import time
import time
from scraper import scaper
def main():
    x = SMACrossOver()
    y = scaper()
    while True:
        x.tick([80, 40, 0.0005])
        y.tick()
        time.sleep(60)

if __name__ == "__main__":
    main()
