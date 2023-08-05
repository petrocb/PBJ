import numpy as np
def volatility(pastPrices, period):
    vol = np.std(pastPrices) * np.sqrt(period)
    return vol

def priceDensity(pastPrices,period):
    pass