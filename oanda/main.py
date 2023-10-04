import requests
from EMACrossOver import EMACrossOver
from SMACrossOver import SMACrossOver
import functions
import json
import time
import backtrader
import time
from scraper import scaper
def main():
    x = scaper()
    while True:
        x.tick()
        time.sleep(10)

if __name__ == "__main__":
    main()
