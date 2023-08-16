import backtrader as bt
import numpy as np
import matplotlib.pyplot as plt
from backtrader import cerebro
import csv
from diffClacEveryTickStrat import diffClacEveryTickStrat
from diffClacTradeStartStrat import diffClacTradeStartStrat
from staticDiffStrat import staticDiffStrat
from EMACrossoverStrategy import EMACrossoverStrategy
from VWAP_Boll_EMA_Strategy import VWAP_Boll_EMA_Strategy
import summary
from random import randint
#import pandas as pd
#from summary import summary


def save_plot_as_png():
    # Call cerebro.plot() to display the plot
    #cerebro.plot()

    # Find the save button by looking for the 'icon' attribute containing 'filesave' text
    save_button = plt.get_current_fig_manager().toolbar.children()[8]

    # Trigger the button's 'clicked' event
    save_button.trigger('clicked')

    # Close the plot after saving
    plt.close()


def main():

    strats = [EMACrossoverStrategy]
    fxData = ['EURUSD2.csv']
    conditions = []
    for o in range(10):
        for i in range(10):
            conditions.append([(o+1)*10, (i+1)*10])
    for o in strats:
        for m in fxData:
            for i in conditions:
                cerebro = bt.Cerebro()
                arr = []
                cerebro.addstrategy(o, arr=arr, i=m)  # Pass vwap_values
                print("Loading data")
                data = bt.feeds.MT4CSVData(dataname=m, timeframe=bt.TimeFrame.Minutes, compression=1)
                cerebro.adddata(data)
                print("Loading data finished")
                cerebro.run()
                output_text = summary.summary(arr, data)

                with open("output.txt", "a") as file:
                    file.write(str(output_text))
                    file.write('\n')

                #create_html_file("output.html", str(o)+" "+str(m)+" "+str(i)+" "+str(output_text), pic)
                with open("EURUSD2.csv", newline='') as csvfile:
                    csv_reader = csv.reader(csvfile)
                    plotData = [row for row in csv_reader]
                test = []
                for c in plotData:
                    test.append([float(c[2]), float(c[3]), float(c[4]), float(c[5])])
                plt.plot(test)

                #cerebro.plot()
                pic = 'charts/'+str(randint(0,9999999))+'.png'
                plt.savefig(pic)
                #plt.show()
                create_html_file("output.html", str(o) + " " + str(m) + " " + str(i) + " " + str(output_text), pic)
def create_html_file(file_path, text, pic):
    # HTML code as a string
    html_content = f"""
        <div>
        <h1>Result</h1>
        <p>{text.replace("{", "").replace("}", "").replace("'", "")}</p>
        <img src="{pic}">
        <div>
    """

    # Write the HTML content to the file
    with open(file_path, 'a') as html_file:
        html_file.write(html_content)


if __name__ == "__main__":
    print("pea head")
    print("Starting")
    main()
    print("Finished")
    exit(69)