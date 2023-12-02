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
    price: str
    openTime: str
    initialUnits: str
    currentUnits: str
    pl: str


    # Decides how to process an order. If the order is extending a position or if the order is closing a position.
    def getOrder(self, position, trades):
        try:
            if (float(position['positions'][0]['long']['units']) + float(
                    position['positions'][0]['short']['units']) == 0) or (
                    float(position['positions'][0]['long']['units']) > 0 and float(self.initialUnits) > 0) or (
                    float(position['positions'][0]['short']['units']) < 0 and float(self.initialUnits) < 0):
                print({'orderFillTransaction': asdict(self)})
                return {'orderFillTransaction': asdict(self)}
            else:
                unitsLeft = float(self.initialUnits)
                # if float(self.units) > 0:
                pl = float(self.pl)
                for i in trades:
                    pl += float(i.initialUnits) * (float(self.price) - float(i.price))
                    unitsLeft -= float(i.initialUnits)
                self.pl = str(pl)
                print({'orderFillTransaction': asdict(self)})
                return {'orderFillTransaction': asdict(self)}

                # if float(self.units) > 0:
                #     if float(position['positions'][0]['short']['units']) > float(self.units):
                #         for i in trades:
                #
                #     else:
                #         pass
                # elif float(self.units) < 0:
                #     pass

            # else:
            #     units = float(self.units)
            #     for i in trades:
            #         units += float(i.units)
            #         if units == 0:
            #             self.pl = str(float(self.units) * (float(self.price) - float(i.price)))
            #             return {'orderFillTransaction': asdict(self)}
            #         else:
            #             self.pl = str(float(self.units) * (float(self.price) - float(i.price)))
            #             units += float(i.units)
        except IndexError:
            print({'orderFillTransaction': asdict(self)})
            return {'orderFillTransaction': asdict(self)}



    def asdict(self):
        return asdict(self)


@dataclass
class Activity:
    activity: []

    def getActivity(self):
        return self.activity

    def getActivityDict(self):
        return {'transactions': asdict(self)['activity']}

    def setSetActivity(self, activity):
        activity = activity['orderFillTransaction']
        self.activity.append(Trade(activity['id'], activity['price'], activity['openTime'], activity['units'], activity['pl']))


class Account:
    def __init__(self):
        self.activity = Activity([])

    def getActivity(self):
        return self.activity

    def getActivityDict(self):
        return self.activity.getActivityDict()

    def setActivity(self, activity):
        self.activity.setSetActivity(activity)

    def getPosition(self):
        total = 0
        for i in self.getTrades():
            total += float(i.initialUnits)
        if total > 0:
            return Position(Units(str(total)), Units("0")).getPosition()
        elif total < 0:
            return Position(Units("0"), Units(str(total))).getPosition()
        else:
            return Position(Units("0"), Units("0")).getPosition()

    def getTrades(self):
        pos = self.getPosition()
        total = 0
        list = []
        activity = self.getActivity().activity
        for i in activity:
            total += float(i.initialUnits)
            list.append(i)
            if total == 0:
                list = []
        if total == 0:
            return []

        else:
            arr = []
            for i in list:
                arr.append(i)
            return arr

    def getTradesasDict(self):
        total = 0
        list = []
        activity = self.getActivity().activity
        for i in activity:
            total += float(i.initialUnits)
            list.append(i)
            if total == 0:
                list = []
        if total == 0:
            return {'trades': []}

        else:
            arr = []
            for i in list:
                arr.append(i.asdict())
            return {'trades': arr}
