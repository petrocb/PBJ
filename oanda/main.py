import requests
from EMACrossOver import EMACrossOver
import json
def main():
    token = "554a05a67a483b45171693a0ded86b01-7f36009c47bba3095ed7d8cc9901486c"


    accountID = "101-004-25985927-001"
    # response = requests.get("https://stream-fxpractice.oanda.com/v3/accounts/{}/pricing/stream?instruments={}".format(accountID, "EUR_USD"), headers={'Authorization': api}, stream=True)
    price = requests.get(f"https://api-fxpractice.oanda.com/v3/accounts/{accountID}/pricing", headers={'Authorization': f'Bearer {token}'}, params={'instruments': "EUR_USD"})
    print(price)
    print("Response Status Code:", price.status_code)
    print("Response Content:", price.text)
    price = price.json()
    print(price['prices'][0]['bids'][0]['price'])
    print(price['prices'][0]['asks'][0]['price'])
    # x = EMACrossOver()
    # print(api.request(orders.OrderList(accountID)))
    # price = api.request(pricing.PricingInfo(accountID=accountID, params={"instruments": "EUR_USD"}))['prices'][0]
    # print(price)
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



