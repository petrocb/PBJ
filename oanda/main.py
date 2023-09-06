import requests
from EMACrossOver import EMACrossOver
import functions
import json


def main():

    # print(functions.getBid())
    # print(functions.getAsk())
    list = functions.startPastPricesList()
    x = EMACrossOver(list)
    print(list['candles'][-1]['time'])
    #list = functions.updatePastPrices(list)
    # i = False
    # while i:
    #     x.tick()

        #print(price)
if __name__ == "__main__":
    main()


# import json
# import time
# import oandapyV20
# from oandapyV20 import API
# import oandapyV20.endpoints.trades as trades
# import oandapyV20.endpoints.pricing as pricing
# import oandapyV20.endpoints as endpoint
# import oandapyV20
#
# import oandapyV20
# import oandapyV20.endpoints.orders as orders
#
# api = API(access_token="c06b065ec12eccbd47f70fea52c15aac-d625e4fa12ac970a43ea6dd82c5d6f84")
# accountID = "101-004-25985927-001"
# ask = 0
# bid = 0
# sell = {
#   "order": {
#     "price": str(ask),
#     "instrument": "EUR_USD",
#     "units": "-100",
#     "type": "MARKET"
#   }
# }
# buy = {
#   "order": {
#     "price": str(bid),
#     "instrument": "EUR_USD",
#     "units": "100",
#     "type": "MARKET"
#   }
# }
#
#
#
# print(api.request(orders.OrderList(accountID)))
#
# diff = 0.044
# buyOpen = False
# sellOpen = False
#
# x = True
# while x:
#     startTime = time.perf_counter()
#     for i in range(10):
#         price = api.request(pricing.PricingInfo(accountID=accountID, params={"instruments": "EUR_USD"}))['prices'][0]
#         bid = float(price['bids'][0]['price'])
#         ask = float(price['asks'][0]['price'])
#         newAsk = bid + diff
#         newBid = ask - diff
#         if not buyOpen and not sellOpen:
#             startingAsk = ask
#             startingBid = bid
#             trailingAsk = ask - diff
#             trailingBid = bid - diff
#             buyOpen = True
#             sellOpen = True
#         if trailingAsk < newAsk:
#             trailingAsk = newAsk
#
#         if trailingBid > newBid:
#             trailingBid = newBid
#
#         if trailingAsk > ask and buyOpen and sellOpen:
#             #open sell
#             api.request(orders.OrderCreate(accountID, sell))
#             buyOpen = False
#
#         if trailingBid < bid and buyOpen and sellOpen:
#             #open buy
#             api.request(orders.OrderCreate(accountID, buy))
#             sellOpen = False
#
#         if trailingAsk > ask and buyOpen:
#             #close buy
#             api.request(orders.OrderCreate(accountID, sell))
#             buyOpen = False
#
#         if trailingBid < bid and sellOpen:
#             #close sell
#             api.request(orders.OrderCreate(accountID, buy))
#             sellOpen = False
#
#
#     print(time.asctime(), "bid:", bid, " ask:", ask, " trailingBuy:", trailingAsk, " trailingSell:", trailingBid,
#           " buyOpen:", buyOpen, " sellOpen:", sellOpen, " spread:", round(ask - bid, 5), " in:", round(time.perf_counter()-startTime, 2), "seconds")



