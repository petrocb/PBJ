from dataclasses import asdict
from dataclasses import dataclass
from typing import Optional, List
@dataclass
class Units:
    units: str


@dataclass
class Position:
    long: Units
    short: Units

    def getPosition(self):
        if self.long.units != "0" or self.short.units != "0":
            return {'positions': [asdict(self)]}
        else:
            return {'positions': []}

@dataclass
class Order:
    id: str
    time: str
    units: str
    # takeProfitOnFill: Optional[slTp] = None
    # stopLossOnFill: Optional[slTp] = None
    # trailingStopLossOnFill: Optional[slTp] = None

    def getOrder(self):
        return {'orderFillTransaction': asdict(self)}

@dataclass
class Trade:
    id: str
    # price: str
    openTime: str
    units: str

    def getOrder(self):
        return {'orderFillTransaction': asdict(self)}

class Account:
    def __init__(self):
        self.position = Position(Units("0"), Units("0"))
        self.activity = []
        self.trades = []
        self.id = 0
        self.orders = []

    def setActivity(self, activity):
        self.activity.append(activity)
        # print(self.activity)

    def getPosition(self):
        # total = 0
        # for i in self.activity:
        #     total += float(i['orderFillTransaction']['units'])
        # if total > 0:
        #
        #     return Position(Units(str(total)), Units("0")).getPosition()
        #
        # return Position(Units("0"), Units(str(total))).getPosition()
        print(self.getTrades())
        print(Position(Units(str(self.getTrades()[0]['orderFillTransaction']['units'])), Units("0")).getPosition())
        return Position(Units(str(self.getTrades()[0]['orderFillTransaction']['units'])), Units("0")).getPosition()

    def getTrades(self):
        total = 0
        trades = []
        for i in self.activity:
            total += float(i['orderFillTransaction']['units'])
            trades.append(i)
            if total == 0:
                trades = []

        if total == 0:
            return [Trade("0", "0", "0").getOrder()]

        else:
            return trades
        # try:
        #     return self.activity[-1]
        # except IndexError:
        #     return Trade("0", "0", "0").getOrder()

