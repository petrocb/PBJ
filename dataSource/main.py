import requests
import pandas as pd

def getCred(account):
    if account == 'primary':
        return ["https://api-fxpractice.oanda.com", "2a35930fb4d1eaf4b032d8822367d6ab-2563dd26343f638eb8366e58a0e8718c",
                "101-004-25985927-001"]

def scrapper(count, instrument, timeFrame):
    oCount = count
    list = []
    prices = []
    if count > 5000:
        for o in range((count + 5000) // 5000 - 1):
            if count > 5000:
                tempCount = 5000
                count -= 5000
            else:
                tempCount = count
            if o == 0:
                data = requests.get(
                    f"{getCred('primary')[0]}/v3/accounts/{getCred('primary')[2]}/instruments/{instrument}/candles",
                    headers={'Authorization': f"Bearer {getCred('primary')[1]}"},
                    params={'granularity': timeFrame, 'count': tempCount})
            else:
                data = requests.get(f"{getCred('primary')[0]}/v3/accounts/{getCred('primary')[2]}/instruments/{instrument}/candles",
                                    headers={'Authorization': f"Bearer {getCred('primary')[1]}"},
                                    params={'granularity': timeFrame, 'count': tempCount, 'to': prices[0][0]})
            data = data.json()
            data = data['candles']
            prices = []
            for i in data:
                prices.append([i['time'], i['mid']['o'], i['mid']['h'], i['mid']['l'], i['mid']['c'], i['volume']])
            list = prices + list
            print(count)
    else:
        data = requests.get(
            f"{getCred('primary')[0]}/v3/accounts/{getCred('primary')[2]}/instruments/{instrument}/candles",
            headers={'Authorization': f"Bearer {getCred('primary')[1]}"},
            params={'granularity': timeFrame, 'count': count})
        data = data.json()
        print(data)
        data = data['candles']
        prices = []
        for i in data:
            prices.append([i['time'], i['mid']['o'], i['mid']['h'], i['mid']['l'], i['mid']['c'], i['volume']])
        list = prices + list
        print(count)
    prices = pd.DataFrame(list)
    prices.columns = ['Date', 'Open', 'High', 'Low', 'Close', 'Volume']
    # prices.to_csv("NewData/"+instrument+timeFrame+str(datetime.datetime.now()).replace(" ", "").replace(".", "")
    #               .replace("-", "").replace(":", "")+'.csv', index=False, header=False)
    print(prices['Date'].iloc[-1])
    prices.to_csv(f"NewData/{instrument}_{timeFrame}_{str(prices['Date'].iloc[-1])[:19]}_{str(prices['Date'].iloc[0])[:19]}_{oCount}".replace(".", "_").replace("-", "_").replace(":", "_")+".csv", index=False, header=False)

    return prices

if __name__ == '__main__':
    scrapper(2000, "EUR_USD", "D")