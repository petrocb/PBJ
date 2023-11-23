from dataclasses import dataclass
from dataclasses import asdict
from typing import Optional, List


@dataclass
class slTp:
    distance: str


@dataclass
class Order:
    id: str
    time: str
    units: str
    takeProfitOnFill: Optional[slTp] = None
    stopLossOnFill: Optional[slTp] = None
    trailingStopLossOnFill: Optional[slTp] = None

    def getOrder(self):
        return {'orderFillTransaction': asdict(self)}


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
class Activity:
    pass

@dataclass
class Trade:
    id: str
    price: str
    openTime: str
    initialUnits: str
@dataclass
class Trades:
    trades: Optional[List[Trade]] = []


class Account:
    position: Optional[Position] = Position(Units("0"), Units("0"))
    activty: Optional[Activity] = Activity()
    trades: Optional[Trades] = []
