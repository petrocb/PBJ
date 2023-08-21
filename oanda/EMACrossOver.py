import requests
import json
class EMACrossOver():
    def __init__(self):
        self.buyOpen = False
        self.sellOpen = False
        self.shortEma = 0
        self.longEma = 0
    def tick(self):
        pass

    def getCred(self):
        return ["https://api-fxpractice.oanda.com", "554a05a67a483b45171693a0ded86b01-7f36009c47bba3095ed7d8cc9901486c", "101-004-25985927-001"]

    def getPrice(self):
        price = requests.get(f"{self.getCred()[0]}/v3/accounts/{self.getCred()[2]}/pricing",
                             headers={'Authorization': f'Bearer {self.getCred()[1]}'},
                             params={'instruments': "EUR_USD"})

        price = price.json()
        price = price['prices'][0]
        return price

    def getBid(self):
        return self.getPrice()['bids'][0]['price']
    def getAsk(self):
        return self.getPrice()['asks'][0]['price']