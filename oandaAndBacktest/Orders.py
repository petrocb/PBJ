from dataclasses import asdict
from dataclasses import dataclass
from typing import Optional


@dataclass
class slTp:
    distance: str


@dataclass
class Orders:
    id: str
    time: str
    units: str
    takeProfitOnFill: Optional[slTp] = None
    stopLossOnFill: Optional[slTp] = None
    trailingStopLossOnFill: Optional[slTp] = None

    def getOrder(self):
        return asdict(self)
