def rsi(data, period):
    delta = data.diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()

    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

def sma(data):
    list = []
    for i in data:
        list.append(i[1])
    # print(len(list))
    return sum(list) / len(list)