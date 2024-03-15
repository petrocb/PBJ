from random import randint
from .. import functions
class randomDirection2:
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
        # print("pos", position)
        r = randint(-5, 5)
        if r == 5:
            r = 1
        elif r == -5:
            r = -1
        else:
            r = 0
        if (position == 0) or (position < 0 and r == 1) or (position > 0 and r == -1):
            # print("dir", r)
            functions.marketOrder(500 * r, self.account, self.account, 0, 0, 0)





