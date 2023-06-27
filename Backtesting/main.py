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
    return np.unique(ts)


def EMA2(p, window_LT=200, window_ST=50, signal_type='buy',):
    alpha_LT = 2 / (window_LT + 1)
    beta_LT = 1 - alpha_LT
    alpha_ST = 2 / (window_ST + 1)
    beta_ST = 1 - alpha_ST
    signals = np.zeros(len(p))
    sl = np.zeros(len(p))
    ent = np.zeros(len(p))

    ema_LT = np.zeros(len(p))
    ema_ST = np.zeros(len(p))


    if len(p) < window_LT:
        return pd.DataFrame({'signals': signals, 'Price':p,'Entry':ent,'Stop Loss':sl})

    ema_LT[window_LT] = np.average(p[:window_LT])
    ema_ST[window_ST] = np.average(p[:window_ST])



    for i in range(window_LT + 1, len(p)):
        ema_LT[i] = (alpha_LT * p[i]) + (ema_LT[i - 1] * beta_LT)

    for i in range(window_ST + 1, len(p)):
        ema_ST[i] = (alpha_ST * p[i]) + (ema_ST[i - 1] * beta_ST)

    # Defining Stop Loss
    for i in range(window_LT, len(p) - 1):
        if (ema_ST[i - 1] < ema_LT[i - 1] or ema_LT[i - 1] == 0) and ema_ST[i] > ema_LT[i]:
           sl[i] = p[i]-0.0020
        elif ema_ST[i] > ema_LT[i] and ema_ST[i - 1] > ema_LT[i - 1] and p[i]<=p[i-1]:
            sl[i]=  sl[i-1]
        elif ema_ST[i] > ema_LT[i] and ema_ST[i - 1] > ema_LT[i - 1] and p[i]>p[i-1]:
            sl[i]=  p[i]-0.0020
        else:
            sl[i] = 0



    #Define trade entry and exit
    for i in range(window_LT, len(p) - 1):

        if ema_ST[i] > ema_LT[i] and ema_ST[i-1] < ema_LT[i-1] and signal_type =='buy':
            signals[i] = 1
        elif ema_ST[i] > ema_LT[i] and  ema_ST[i-1] > ema_LT[i-1] and p[i]>sl[i]:
            signals[i] = 1


        # elif ema_ST[i] < ema_LT[i] and p[i]<sl[i] and signal_type == 'sell':
        #     signals[i] = -1

    #Defining Entry Price

    for i in range(window_LT, len(p) - 1):
        if ema_ST[i - 1] < ema_LT[i - 1] and ema_ST[i] > ema_LT[i] and signal_type =='buy':
           ent[i] = p[i]
        elif signals[i-1]==1 and signals[i]==1:
            ent[i] = ent[i-1]

    return pd.DataFrame({'signals': signals, 'ema_LT': ema_LT, 'ema_st': ema_ST, 'Price': p, 'Entry': ent, 'Stop Loss': sl})


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


def trail(p,t,m):
#p= price data, t=time periods used to take volitility, m=multiple can chose this
    signals = np.zeros(len(p))
    diff = np.zeros(len(p))
    sl = np.zeros(len(p))
    ent = np.zeros(len(p))
    if len(p) < t:
        return pd.DataFrame({'signals': signals, 'Price': p, 'Diff':diff, 'Entry': ent, 'Stop Loss': sl})



    for i in range(t, len(p) ):
      diff[i] = np.std(p[i-t:i]) * np.sqrt(t) * m



    # Defining Stop Loss
    for i in range(t, len(p) - 1):
        if p[i] > p[i-1] + (diff[i-1]) and diff[i-1]>0:
           sl[i] = p[i]-0.0020
        elif p[i] > sl[i-1] and sl[i-1]>0:
            sl[i]= max((p[i]-p[i-1]+sl[i-1]),sl[i-1])
        else:
            sl[i] = 0

    for i in range(t, len(p) - 1):
        if p[i] > (p[i-1] + (diff[i-1])) and diff[i-1]>0:
            signals[i] = 1
        elif p[i]>sl[i-1] and sl[i-1]>0:
            signals[i]=1

    # Defining Entry Price

    for i in range(t, len(p) - 1):
         if signals[i]==1 and signals[i-1]==0:
                ent[i] = p[i]
         elif signals[i - 1] == 1 and signals[i] == 1:
                ent[i] = ent[i - 1]

    return pd.DataFrame({'signals': signals, 'Price': p, 'Diff':diff, 'Entry': ent, 'Stop Loss': sl})



''' sample code: test EMA (1-min/5-min data) '''
#dat = pd.read_csv('/Users/jackjones/Desktop/Python Projects/Backtesting/EURUSD.csv', index_col=False, parse_dates={'Datetime': ['Date', 'Time']})
dat = pd.read_csv('/Users/jackjones/Desktop/Python Projects/Backtesting/EURUSD.csv')
dat = dat.rename(columns={'1999.01.04': 'Date', '09:22': 'Time','1.18010':'Open', '1.18190':'High','1.18010.1':'Low','1.18170':'Close','4':'Volume'})
#Only pull 2023 data
dat = dat[dat['Date'].str.contains("2023")]
dat = dat.set_index('Date')



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
  this_dat = dat.loc[dat.index == d]

# find the number of observations in date d
  summary_table.loc[d]['Num. Obs.'] = this_dat.shape[0]
    # get trading (i.e. position holding) signals
  trade_entry= trail(this_dat['Close'],5,0.25)
  # trade_entry = EMA2(this_dat['Open'], window_LT=1000, window_ST=500, signal_type='buy')
  trade_entry['Time'] = this_dat['Time']

  signals = trade_entry['signals']



  # find the number of trades in date d
  summary_table.loc[d]['Num. Trade'] = np.sum(np.diff(signals) == 1)
    # find PnLs for lot size 5000
  lot_size = 5000
  signals_padded = np.concatenate(([0], signals))
  summary_table.loc[d]['PnL'] = np.sum(-lot_size * this_dat['Close'] * np.diff(signals_padded))
  # find the win ratio NEED TO RECONFIG FOR FOREX
  ind_in = np.where(np.diff(signals) == 1)[0] + 1
  ind_out = np.where(np.diff(signals) == -1)[0] + 1
  num_win = np.sum((this_dat['Close'].values[ind_out] - this_dat['Close'].values[ind_in]) > 0)
  if summary_table.loc[d]['Num. Trade'] != 0:
    summary_table.loc[d]['Win. Ratio'] = 1. * num_win / summary_table.loc[d]['Num. Trade']

    # HOLDING WINDOW
    #columns = ['signals', 'shift', 'Count']
    #window_count = pd.DataFrame(columns=columns)
    #window_count['signals'] = signals
    #window_count['shift'] = window_count['signals'].shift()
    #empt = []
    #cnt = 1
    #for i in np.arange(len(signals) - 1):
     #   if window_count['signals'][i] == window_count['shift'][i] == 1:
      #      cnt += 1
       # else:
        #    cnt = 1
        #empt.append(cnt)
    #empt.append(1)
    #window_count['Count'] = empt

    #window_count['Close'] = np.zeros(len(signals))
    #for i in np.arange(len(signals)):
     #   if window_count.loc[i, 'signals'] == 1 and window_count.loc[i + 1, 'signals'] == 0:
     #       window_count.loc[i, 'close'] = 1

    #summary_table.loc[d]['Max Holding Window'] = window_count['Count'][window_count['Close'] == 1].max()
    #summary_table.loc[d]['Min Holding Window'] = window_count['Count'][window_count['Close'] == 1].min()
    #summary_table.loc[d]['Average Holding Window'] = window_count['Count'][window_count['Close'] == 1].mean()

Total_PnL = summary_table['PnL'].sum()
Total_win_loss = (summary_table['Win. Ratio'] * summary_table['Num. Trade']).sum() / summary_table['Num. Trade'].sum()
