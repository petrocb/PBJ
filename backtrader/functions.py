import numpy
def diffCalc(pastPrices):
    vol = np.std(pastPrices) * np.sqrt(20)
    return vol * 10