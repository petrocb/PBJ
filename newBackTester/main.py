from EMACrossOver import EMACrossOver
from summary import summary
import pandas as pd
import numpy as np
from functions import EMA2
from functions import signals
import csv
def main():
    lot_size = 10000
    direction = 'sell only'
    # close_data = np.array([1.0700,1.0695,1.0685,1.0680,1.0679,1.0675,1.0670,1.0665,1.0664,1.0663,1.0660,1.0650,1.0640,1.0615,1.0618,1.0622,1.0627,1.0630,1.0635,1.06637,1.0640])
    #2023.04.07, 15: 11, 1.09196, 1.09206, 1.09193, 1.09206, 17
    #open,high,low,close
    data = pd.read_csv('EURUSD3.csv')
    date= data['2023.04.07']
    time= data['15:11']
    close_data = data['1.09206']
    #print(close_data)

    df = EMA2(close_data,10,30,direction)
    print(df)

    obs = close_data.shape[0]

    num_trades = np.sum(np.diff(df['Signals'])==1)

    ind_in = np.where(np.diff(df['Signals'])==1)[0]+1
    ind_out = np.where(np.diff(df['Signals'])==-1)[0]+1
    ind_in_price= close_data[ind_in].reset_index(drop=True)
    ind_in_date= date[ind_in].reset_index(drop=True)
    ind_in_time= time[ind_in].reset_index(drop=True)
    ind_out_price= close_data[ind_out].reset_index(drop=True)
    ind_out_date= date[ind_out].reset_index(drop=True)
    ind_out_time= time[ind_out].reset_index(drop=True)
    if direction == 'sell only':
        pnl= ind_in_price - ind_out_price
    else:
        pnl = ind_out_price - ind_in_price

    in_vs_out= pd.DataFrame(data={'Date IN': ind_in_date , 'Time IN':ind_in_time ,'Price IN':ind_in_price,'Date OUT':ind_out_date , 'Time OUT': ind_out_time, 'Price OUT': ind_out_price, 'PnL': pnl})
    print(in_vs_out)
    #value when getting in must be bigger than getting out as we are SELLING
    #switch this if buying


    if direction == 'sell only':
         num_win = np.sum((in_vs_out['Price IN']-in_vs_out['Price OUT'])>0)
    elif direction == 'buy only':
         num_win = np.sum((in_vs_out['Price OUT'] - in_vs_out['Price IN']) > 0)
    if  num_trades != 0:
        win_ratio = num_win/num_trades
    else:
        win_ratio = 0

    summary_data = {'Num. Obs.': obs, 'Num. Trade': num_trades, 'Pnl':sum(pnl)*lot_size, "Win Ratio": win_ratio}  # add addtional fields if necessary
    summary_table = pd.DataFrame(data=summary_data, index=[0])
    print(summary_table)
















    # print(signals(df,8))
    # print(np.diff(signals(df,8)))

    #print(signals(EMA2(data,8,3),"sell only"))
    #runOrder = 1
    #strats = [EMACrossOver()]
    #fxData = ['EURUSD2.csv']
    #conditions = [0]
    #data = []
    #for o in strats:
        #for m in fxData:
            #for i in conditions:
                #with open('EURUSD2.csv', newline='') as csvfile:
                    #reader = csv.reader(csvfile, delimiter=',', quotechar='|')
                    #count = 0
                    #for x in reader:
                # arr = []
                # plotData = []
                # for x in m:
                        #try:
                            #o.tick()
                        #except TypeError as e:
                            #print(e)
                #summary(getPositions(), data)


if __name__ == "__main__":
    main()
