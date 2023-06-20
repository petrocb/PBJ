import pandas as pd
import numpy as np
from datetime import datetime

#import yfinance as yf


# # set dates
# sd = datetime(2023, 5, 8)
# ed = datetime(2023, 6, 5)
#
# # GBPUSD15M
# df = yf.download(tickers='GBPUSD=X', start=sd, end=ed, interval="15m")
# df.to_csv('GBPUSD_15m.csv')
# # GBPUSD5M
# df = yf.download(tickers='GBPUSD=X', start=sd, end=ed, interval="5m")
# df.to_csv('GBPUSD_5m.csv')
# # GBPUSD2M
# df = yf.download(tickers='GBPUSD=X', start=sd, end=ed, interval="2m")
# df.to_csv('EURUSD_2m.csv')


def get_dates(ts):
    # input Datetime as DataFrame index
    # return a list of dates in the dataset
    return np.unique(ts.date)


def EMA2(p, window_LT=200, window_ST=50, signal_type='buy'):
    alpha_LT = 2 / (window_LT + 1)
    beta_LT = 1 - alpha_LT
    alpha_ST = 2 / (window_ST + 1)
    beta_ST = 1 - alpha_ST
    signals = np.zeros(len(p))
    if len(p) < window_LT:
        return signals

    ema_LT = np.zeros(len(p))
    ema_ST = np.zeros(len(p))
    ema_LT[window_LT] = np.average(p[:window_LT])
    ema_ST[window_ST] = np.average(p[:window_ST])

    for i in range(window_LT + 1, len(p)):
        ema_LT[i] = (alpha_LT * p[i]) + (ema_LT[i - 1] * beta_LT)

    for i in range(window_ST + 1, len(p)):
        ema_ST[i] = (alpha_ST * p[i]) + (ema_ST[i - 1] * beta_ST)

    for i in range(window_LT, len(p) - 1):

        if ema_ST[i] > ema_LT[i] and signal_type == 'buy':
            signals[i] = 1
        elif ema_ST[i] < ema_LT[i] and signal_type == 'sell':
            signals[i] = -1

        # if ema_ST[i - 1] < ema_LT[i - 1] and ema_ST[i] > ema_LT[i]:
        # signals[i] = -1
        # elif ema_ST[i - 1] > ema_LT[i - 1] and ema_ST[i] < ema_LT[i]:
        # signals[i] = 1

    return signals


def SMA2(p, window_LT=200, window_ST=50, signal_type='buy'):
    signals = np.zeros(len(p))
    if len(p) < window_LT:
        return signals

    sma_LT = np.zeros(len(p))
    sma_ST = np.zeros(len(p))

    sma_LT[window_LT - 1:] = [np.average(p[i - window_LT + 1:i + 1]) for i in range(window_LT - 1, len(p))]
    sma_ST[window_ST - 1:] = [np.average(p[i - window_ST + 1:i + 1]) for i in range(window_ST - 1, len(p))]

    for i in range(window_LT, len(p) - 1):
        if sma_ST[i] > sma_LT[i] and signal_type == 'buy':
            signals[i] = 1
        elif sma_ST[i] < sma_LT[i] and signal_type == 'sell':
            signals[i] = -1

    return signals


''' sample code: test EMA (1-min/5-min data) '''

dat = pd.read_csv('C:/Users/St Potrock/Desktop/EURUSD2.csv', index_col=False, parse_dates={'Datetime': ['date', 'time']}, date_format='%Y.%m.%d %H:%M')
dat = dat.set_index('Datetime')

#
# dat = pd.read_csv('C:/Users/St Potrock/Desktop/EURUSD2.csv')
# print(dat.iloc[0])
dates = get_dates(dat.index)

# create a summary table
cols = ['Num. Obs.', 'Num. Trade', 'PnL', 'Win. Ratio', 'Average Holding Window',
        'Max Holding Window', 'Min Holding Window']  # add addtional fields if necessary
summary_table = pd.DataFrame(index=dates, columns=cols)
# loop backtest by dates
for d in dates:
    this_dat = dat.loc[dat.index.date == d]
    # find the number of observations in date d
    summary_table.loc[d]['Num. Obs.'] = this_dat.shape[0]
    # get trading (i.e. position holding) signals
    signals = EMA2(this_dat['close'], window_LT=20, window_ST=9, signal_type='buy')

    # find the number of trades in date d
    summary_table.loc[d]['Num. Trade'] = np.sum(np.diff(signals) == 1)
    # find PnLs for lot size 5000
    lot_size = 10000
    signals_padded = np.concatenate(([0], signals))
    summary_table.loc[d]['PnL'] = np.sum(-lot_size * this_dat['close'] * np.diff(signals_padded))
    # find the win ratio NEED TO RECONFIG FOR FOREX
    ind_in = np.where(np.diff(signals) == 1)[0] + 1
    ind_out = np.where(np.diff(signals) == -1)[0] + 1
    num_win = np.sum((this_dat['close'].values[ind_out] - this_dat['close'].values[ind_in]) > 0)
    if summary_table.loc[d]['Num. Trade'] != 0:
        summary_table.loc[d]['Win. Ratio'] = 1. * num_win / summary_table.loc[d]['Num. Trade']

    # HOLDING WINDOW
    columns = ['signals', 'shift', 'Count']
    window_count = pd.DataFrame(columns=columns)
    window_count['signals'] = signals
    window_count['shift'] = window_count['signals'].shift()
    empt = []
    cnt = 1
    for i in np.arange(len(signals) - 1):
        if window_count['signals'][i] == window_count['shift'][i] == 1:
            cnt += 1
        else:
            cnt = 1
        empt.append(cnt)
    empt.append(1)
    window_count['Count'] = empt

    window_count['close'] = np.zeros(len(signals))
    for i in np.arange(len(signals)):
        if window_count.loc[i, 'signals'] == 1 and window_count.loc[i + 1, 'signals'] == 0:
            window_count.loc[i, 'close'] = 1

    summary_table.loc[d]['Max Holding Window'] = window_count['Count'][window_count['close'] == 1].max()
    summary_table.loc[d]['Min Holding Window'] = window_count['Count'][window_count['close'] == 1].min()
    summary_table.loc[d]['Average Holding Window'] = window_count['Count'][window_count['close'] == 1].mean()

Total_PnL = summary_table['PnL'].sum()
Total_win_loss = (summary_table['Win. Ratio'] * summary_table['Num. Trade']).sum() / summary_table['Num. Trade'].sum()
