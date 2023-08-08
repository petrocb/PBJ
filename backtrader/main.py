import backtrader as bt
import numpy as np
import matplotlib.pyplot as plt
from backtrader import cerebro
import csv
from diffClacEveryTickStrat import diffClacEveryTickStrat
from diffClacTradeStartStrat import diffClacTradeStartStrat
from staticDiffStrat import staticDiffStrat
from EMACrossoverStrategy import EMACrossoverStrategy
from customPlot import CustomPlot
import summary
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
    cerebro = bt.Cerebro()
    strats = [EMACrossoverStrategy]
    fxData = ['EURUSD2.csv']
    conditions = [0]
    for o in strats:
        for m in conditions:
            for i in fxData:
                arr = []
                cerebro.addstrategy(o, arr=arr)
                print("Loading data")
                data = bt.feeds.MT4CSVData(dataname=i, timeframe=bt.TimeFrame.Minutes, compression=1)
                cerebro.adddata(data)
                print("Loading data finished")
                cerebro.run()
                output_text = summary.summary(arr, data)

                with open("output.txt", "a") as file:
                    file.write(str(output_text))
                    file.write('\n')

                create_html_file("output.html", str(o)+" "+str(m)+" "+str(i)+" "+str(output_text))
    with open("EURUSD2.csv", newline='') as csvfile:
        csv_reader = csv.reader(csvfile)
        data = [row for row in csv_reader]
    x = [[1, 2, 3, 4, 5],[2, 4, 6, 8, 10]]
    y = [2, 4, 6, 8, 10]
    test = []
    for o in data:
        test.append([float(o[2]), float(o[3]), float(o[4]), float(o[5])])
    print(test)
    plt.plot(test)
    cerebro.plot()
    plt.show()
def create_html_file(file_path, text):
    # HTML code as a string
    html_content = f"""
        <h1>Result</h1>
        <p>{text.replace("{", "").replace("}", "").replace("'", "")}</p>
        <img src="{"www"}">
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