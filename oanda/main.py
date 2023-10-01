import requests
from EMACrossOver import EMACrossOver
from SMACrossOver import SMACrossOver
import functions
import json
import time
import backtrader
import time
def main():
    x = SMACrossOver()
    while True:
        x.tick()  # Execute the EMA crossover strategy
        time.sleep(60)  # Sleep for 1 min

if __name__ == "__main__":
    main()
