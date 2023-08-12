import datetime


def spread(oldData):
    data = []
    for i in oldData:
        data.append([i[0], i[1], float(i[5]) - 0.0001, float(i[5]) + 0.0001, i[6]])
    return data


def upOrDown(data):
    for o in range(len(data)-1):
        for i in [1, 5, 15, 30, 60, 120, 240, 480, 720, 1440]:
            try:
                if data[o][2] < data[o + i][2]:
                    data[o].append("u")
                elif data[o][2] > data[o + i][2]:
                    data[o].append("d")
                elif data[o][2] == data[o + i][2]:
                    data[o].append("e")
            except:
                pass
    return data
