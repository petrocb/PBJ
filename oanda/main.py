import requests
from EMACrossOver import EMACrossOver
from SMACrossOver import SMACrossOver
from newSMACross import NewSMACross
import functions
import json
import time
import time
from scraper import scaper
def main():
    x = NewSMACross([30, 10, 0.0005, 0.0005])
    y = scaper()
    while True:
        x.tick()
        y.tick()
        time.sleep(60)

if __name__ == "__main__":
    main()
