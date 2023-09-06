import requests
import json
import datetime


def getCred():
    return ["https://api-fxpractice.oanda.com", "554a05a67a483b45171693a0ded86b01-7f36009c47bba3095ed7d8cc9901486c",
            "101-004-25985927-001"]


def getPrice():
    price = requests.get(f"{getCred()[0]}/v3/accounts/{getCred()[2]}/pricing",
                         headers={'Authorization': f'Bearer {getCred()[1]}'},
                         params={'instruments': "EUR_USD"})

    price = price.json()
    price = price['prices'][0]
    return price


def getBid():
    return getPrice()['bids'][0]['price']


def getAsk():
    return getPrice()['asks'][0]['price']


def startPastPricesList():
    time = datetime.datetime.utcnow() - datetime.timedelta(minutes=5)
    prices = requests.get(f"{getCred()[0]}/v3/accounts/{getCred()[2]}/instruments/EUR_USD/candles",
                          headers={'Authorization': f'Bearer {getCred()[1]}'},
                          params={'granularity': 'M5', 'count': 30})
    prices = prices.json()
    close_prices = [candle['mid']['c'] for candle in prices['candles']]
    return close_prices


def updatePastPrices(prices_list):
    time = datetime.datetime.utcnow() - datetime.timedelta(minutes=5)
    latest_prices = requests.get(f"{getCred()[0]}/v3/accounts/{getCred()[2]}/instruments/EUR_USD/candles",
                                 headers={'Authorization': f'Bearer {getCred()[1]}'},
                                 params={'granularity': 'M5', 'count': 30})

    latest_prices = latest_prices.json()
    latest_candles = latest_prices['candles']
    latest_close_prices = [candle['mid']['c'] for candle in latest_candles]

    # Remove excess data to keep only the last 30 close prices
    if len(prices_list) + len(latest_close_prices) > 30:
        num_to_remove = len(prices_list) + len(latest_close_prices) - 30
        prices_list = prices_list[num_to_remove:]

    # Extend the prices_list with the new close prices
    prices_list.extend(latest_close_prices)
    return prices_list


# Example usage:
past_close_prices = startPastPricesList()
print("Initial Past Close Prices:")
print(past_close_prices)

# Simulate updating past close prices
past_close_prices = updatePastPrices(past_close_prices)
print("\nUpdated Past Close Prices (Last 30 Close Prices):")
print(past_close_prices)
