from dataclasses import asdict
from dataclasses import dataclass


@dataclass
class Units:
    units: str


@dataclass
class Position:
    long: Units
    short: Units

    def getPosition(self):
        return asdict(self)
