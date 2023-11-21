from dataclasses import dataclass
from dataclasses import asdict

@dataclass
class Units:
    units: str

@dataclass
class Position:
    long: Units
    short: Units

    def getPosition(self):
        return asdict(self)
