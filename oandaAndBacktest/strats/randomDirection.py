from random import randint
from .. import functions
class randomDirection:
    def __init__(self, account, sld, tpd, tsld):
        self.account = account
        self.sld = sld
        self.tpd = tpd
        self.tsld = tsld
        # self.data = functions.startPastPricesList(104, "EUR_USD", "W", self.account)

    def tick(self):
        if self.account == "test":
            functions.update()
        # self.data = functions.updatePastPrices2(self.data, 104, "EUR_USD", "W", self.account)
        position = functions.getPositions(self.account)['positions']
        if position:
            position = float(position[0]['long']['units']) + float(position[0]['short']['units'])
        else:
            position = 0
        print("pos", position)
        if position == 0:
            r = randint(-1, 1)
            print("dir", r)
            functions.marketOrder(500 * r, self.account, self.account, self.sld, self.tpd, self.tsld)
