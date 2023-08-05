import backtrader as bt
import numpy as np
import matplotlib.pyplot as plt
from diffClacEveryTickStrat import diffClacEveryTickStrat
from diffClacTradeStartStrat import diffClacTradeStartStrat
from staticDiffStrat import staticDiffStrat
from EMACrossoverStrategy import EMACrossoverStrategy
import summary
#import pandas as pd
#from summary import summary

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

                #print(cerebro.broker.getvalue())
                #print(summary.summary(arr, data))
                # img_path = "plot.png"
                # plt.figure(figsize=(12, 8))
                # x = cerebro.plot()
                # print(type(x))
                #img_path = f"plot_{o.__name__}_{i}.png"

                # Get the plot figure using cerebro.plot()
                #fig = cerebro.plot(style='candlestick', barup='lime', bardown='red')
                cerebro.plot()
                #cerebro.run()

                # img_path = f"plot_{o.__name__}_{i}.png"
                #
                # # Save the plot as a PNG image using plt.savefig()
                # plt.savefig(img_path)
                #
                # output_text = summary.summary(arr, data)
                # Save the plot as a PNG image using PIL
                # plt.savefig("temp_plot.png")  # Save the plot to a temporary file
                # plt.close()
                # plt.savefig(img_path)  # Save the plot before calling plt.show() or plt.close()
                # plt.close()
                output_text = summary.summary(arr, data)

                with open("output.txt", "a") as file:
                    file.write(str(output_text))
                    file.write('\n')

                create_html_file("output.html", str(o)+" "+str(m)+" "+str(i)+" "+str(output_text), example_image_path)
def create_html_file(file_path, text, image_path):
    # HTML code as a string
    html_content = f"""
        <h1>Result</h1>
        <p>{text.replace("{", "").replace("}", "").replace("'", "")}</p>
        <img src="{image_path}" alt="My Image">
    """

    # Write the HTML content to the file
    with open(file_path, 'a') as html_file:
        html_file.write(html_content)

# Example usage
example_text = "This is an example text. You can include multiple paragraphs."
example_image_path = "path/to/your/image.jpg"





if __name__ == "__main__":
    print("pea head")
    print("Starting")
    main()
    print("Finished")
    exit(69)