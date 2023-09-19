import pandas as pd
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
    data = requests.get(f"{getCred()[0]}/v3/accounts/{getCred()[2]}/instruments/EUR_USD/candles",
                        headers={'Authorization': f'Bearer {getCred()[1]}'},
                        params={'granularity': 'M5', 'count': 30})
    data = data.json()
    data = data['candles']
    prices = []
    for i in data:
        prices.append([i['time'], i['mid']['o'], i['mid']['h'], i['mid']['l'], i['mid']['c'], 0, 0])
    prices = pd.DataFrame(prices)
    prices.columns = ['Date', 'Open', 'High', 'Low', 'Close', 'Volume', 'OpenInterest']
    return prices['Close']
    return prices



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
# past_close_prices = startPastPricesList()
# print("Initial Past Close Prices:")
# print(past_close_prices)

# Simulate updating past close prices
# past_close_prices = updatePastPrices(past_close_prices)
# print("\nUpdated Past Close Prices (Last 30 Close Prices):")
# print(past_close_prices)

def emaCalc(data):
    ema = data[-1] * (2 / (len(data) + 1))
    data.pop()
    if len(data) > 0:
        ema += emaCalc(data) * (1 - (2 / (len(data) + 1)))
    return ema

def buy_trade():
        # Place a buy trade
        instrument = "EUR:USD"  # Replace with the instrument you want to trade
        units = 100  # Replace with the desired number of units
        data = {
            "order": {
                "instrument": instrument,
                "units": str(units),  # Convert units to string
                "type": "MARKET"  # You can use other order types if needed
            }
        }
        response = requests.post(f"{getCred()[0]}/v3/accounts/{getCred()[2]}/orders",
                                 headers={'Authorization': f'Bearer {getCred()[1]}'},
                                 json=data)
        return response.json()

def sell_trade():
        # Place a sell trade
        instrument = "EUR:USD"  # Replace with the instrument you want to trade
        units = -100  # Replace with the desired number of units (negative for selling)
        data = {
            "order": {
                "instrument": instrument,
                "units": str(units),  # Convert units to string
                "type": "MARKET"  # You can use other order types if needed
            }
        }
        response = requests.post(f"{getCred()[0]}/v3/accounts/{getCred()[2]}/orders",
                                 headers={'Authorization': f'Bearer {getCred()[1]}'},
                                 json=data)
        return response.json()

def close_trade(trade_id):
        # Close an existing trade by trade ID
        response = requests.put(f"{getCred()[0]}/v3/accounts/{getCred()[2]}/trades/{trade_id}/close",
                                headers={'Authorization': f'Bearer {getCred()[1]}'})
        return response.json()


def calculate_ema(data, alpha):
    """
    Calculate the Exponential Moving Average (EMA) of a given dataset.

    Parameters:
    - data: A list or numpy array containing the time series data.
    - alpha: The smoothing factor (usually between 0 and 1). A higher alpha gives more weight to recent data.

    Returns:
    - ema: A list containing the EMA values.
    """

    if not isinstance(data, (list, np.ndarray)) or len(data) == 0:
        raise ValueError("Data should be a non-empty list or numpy array.")

    if not 0 < alpha <= 1:
        raise ValueError("Alpha should be between 0 and 1.")

    ema = [data[0]]  # The EMA for the first data point is the same as the data point itself

    for i in range(1, len(data)):
        ema_value = alpha * data[i] + (1 - alpha) * ema[-1]
        ema.append(ema_value)

    return ema


# Example usage:
