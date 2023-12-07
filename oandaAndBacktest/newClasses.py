from dataclasses import asdict
from dataclasses import dataclass
from typing import Optional


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
class Trade:
    id: str
    price: str
    openTime: str
    initialUnits: str
    state: str
    currentUnits: str


class Account:
    def __init__(self):
        self.position = Position(Units("0"),Units("0"))
        self.trades = 0
        self.transactions = []

