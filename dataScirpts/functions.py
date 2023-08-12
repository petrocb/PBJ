import datetime
import datetime

def spread(oldData):
    data = []
    for i in oldData:
        data.append([i[0], i[1], round(float(i[5]) - 0.0001, 5), round(float(i[5]) + 0.0001, 5), i[6]])
    return data


def upOrDown(data):
    for o in range(len(data)-1):
        for i in [30]:
            try:
                if data[o][2] < data[o + i][2]:
                    data[o].append(1)
                elif data[o][2] > data[o + i][2]:
                    data[o].append(-1)
                elif data[o][2] == data[o + i][2]:
                    data[o].append(0)
            except:
                pass
    return data

def filter(data):
#     for i in range(len(data)):
#         if int(data[i][0][0:4]) < 2020:
#             data.pop(i)
#             print(data[i])
    newData = [row for row in data if int(row[0][0:4]) == 2022]
    return newData


