import csv
import functions
import pandas as pd
def main():
    data = pd.read_csv('data/EUR_USD_M1_2024_04_03T13_09_00_2024_04_02T20_10_00_1000.csv', header=None, names=['time', 'open', 'high', 'low', 'close', 'volume'])
    win = 0
    winAm = 0
    net = 0
    loss = 0
    lossAm = 0
    # for i in range(len(data)):
    #     # print(data['Close'][i])
    #     if i > 2:
    #         # price has gone up and volume has gone up
    #         if data['close'][i-1] - data['close'][i-2] > 0 and data['volume'][i-1] > data['volume'][i-2]:
    #             if data['close'][i] > data['close'][i-1]:
    #                 win += 1
    #                 winAm += data['close'][i] - data['close'][i-1] - 0.0001
    #                 if data['close'][i] - data['close'][i-1] < 0:
    #                     raise Exception("Error")
    #             elif data['close'][i] < data['close'][i-1]:
    #                 loss += 1
    #                 lossAm += data['close'][i] - data['close'][i-1] - 0.0001
    #                 if data['close'][i] - data['close'][i-1] > 0:
    #                     raise Exception("Error")
    #             else:
    #                 lossAm -= 0.0001
    #                 net += 1
    #         # price has gone up and volume has gone down
    #         elif data['close'][i-1] - data['close'][i-2] > 0 and data['volume'][i-1] < data['volume'][i-2]:
    #             if data['close'][i] > data['close'][i-1]:
    #                 loss += 1
    #                 lossAm += data['close'][i-1] - data['close'][i] - 0.0001
    #                 if data['close'][i-1] - data['close'][i] > 0:
    #                     raise Exception("Error")
    #             elif data['close'][i] < data['close'][i-1]:
    #                 win += 1
    #                 winAm += data['close'][i-1] - data['close'][i] - 0.0001
    #                 if data['close'][i-1] - data['close'][i] < 0:
    #                     raise Exception("Error")
    #             else:
    #                 lossAm -= 0.0001
    #                 net += 1
    #         # price has gone down and volume has gone up
    #         elif data['close'][i-1] - data['close'][i-2] < 0 and data['volume'][i-1] > data['volume'][i-2]:
    #             if data['close'][i] > data['close'][i-1]:
    #                 loss += 1
    #                 lossAm += data['close'][i-1] - data['close'][i] - 0.0001
    #                 if data['close'][i-1] - data['close'][i] > 0:
    #                     raise Exception("Error")
    #             elif data['close'][i] < data['close'][i-1]:
    #                 win += 1
    #                 winAm += data['close'][i-1] - data['close'][i] - 0.0001
    #                 if data['close'][i-1] - data['close'][i] < 0:
    #                     raise Exception("Error")
    #             else:
    #                 lossAm -= 0.0001
    #                 net += 1
    #         # price has gone down and volume has gone down
    #         elif data['close'][i-1] - data['close'][i-2] < 0 and data['volume'][i-1] < data['volume'][i-2]:
    #             if data['close'][i] > data['close'][i-1]:
    #                 win += 1
    #                 winAm += data['close'][i] - data['close'][i-1] - 0.0001
    #                 if data['close'][i] - data['close'][i-1] < 0:
    #                     raise Exception("Error")
    #             elif data['close'][i] < data['close'][i-1]:
    #                 loss += 1
    #                 lossAm += data['close'][i] - data['close'][i-1] - 0.0001
    #                 if data['close'][i] - data['close'][i-1] > 0:
    #                     raise Exception("Error")
    #             else:
    #                 lossAm -= 0.0001
    #                 net += 1

    for i in range(len(data)):
        # print(data['Close'][i])
        if i > 2:
            # price has gone up and volume has gone up
            if data['close'][i] - data['close'][i-1] > 0 and data['volume'][i-1] > data['volume'][i-1]:
                if data['close'][i] > data['close'][i-1]:
                    win += 1
                    winAm += data['close'][i] - data['close'][i-1] - 0.0001
                    if data['close'][i] - data['close'][i-1] < 0:
                        raise Exception("Error")
                elif data['close'][i] < data['close'][i-1]:
                    loss += 1
                    lossAm += data['close'][i] - data['close'][i-1] - 0.0001
                    if data['close'][i] - data['close'][i-1] > 0:
                        raise Exception("Error")
                else:
                    lossAm -= 0.0001
                    net += 1
            # price has gone up and volume has gone down
            elif data['close'][i] - data['close'][i-1] > 0 and data['volume'][i] < data['volume'][i-1]:
                if data['close'][i] > data['close'][i-1]:
                    loss += 1
                    lossAm += data['close'][i-1] - data['close'][i] - 0.0001
                    if data['close'][i-1] - data['close'][i] > 0:
                        raise Exception("Error")
                elif data['close'][i] < data['close'][i-1]:
                    win += 1
                    winAm += data['close'][i-1] - data['close'][i] - 0.0001
                    if data['close'][i-1] - data['close'][i] < 0:
                        raise Exception("Error")
                else:
                    lossAm -= 0.0001
                    net += 1
            # price has gone down and volume has gone up
            elif data['close'][i] - data['close'][i-1] < 0 and data['volume'][i] > data['volume'][i-1]:
                if data['close'][i] > data['close'][i-1]:
                    loss += 1
                    lossAm += data['close'][i-1] - data['close'][i] - 0.0001
                    if data['close'][i-1] - data['close'][i] > 0:
                        raise Exception("Error")
                elif data['close'][i] < data['close'][i-1]:
                    win += 1
                    winAm += data['close'][i-1] - data['close'][i] - 0.0001
                    if data['close'][i-1] - data['close'][i] < 0:
                        raise Exception("Error")
                else:
                    lossAm -= 0.0001
                    net += 1
            # price has gone down and volume has gone down
            elif data['close'][i] - data['close'][i-1] < 0 and data['volume'][i] < data['volume'][i-1]:
                if data['close'][i] > data['close'][i-1]:
                    win += 1
                    winAm += data['close'][i] - data['close'][i-1] - 0.0001
                    if data['close'][i] - data['close'][i-1] < 0:
                        raise Exception("Error")
                elif data['close'][i] < data['close'][i-1]:
                    loss += 1
                    lossAm += data['close'][i] - data['close'][i-1] - 0.0001
                    if data['close'][i] - data['close'][i-1] > 0:
                        raise Exception("Error")
                else:
                    lossAm -= 0.0001
                    net += 1


    print("wins:", win, " losses:", loss, " net:", net)
    print("win amount:", winAm, " loss amount:", lossAm, " total:", winAm + lossAm)
    print((winAm + lossAm) * 500)


if __name__ == "__main__":
    main()
