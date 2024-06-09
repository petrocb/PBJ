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
                    data[o].append(2)
                elif data[o][2] > data[o + i][2]:
                    data[o].append(0)
                elif data[o][2] == data[o + i][2]:
                    data[o].append(1)
            except:
                pass
    return data

def filter(data):
    newData = []
    for row in data:
        if int(row[0][0:4]) > 2022: #and int(row[0][5:7]) == 5:
            newData.append(row)

    # newData = [row for row in data if (int(row[0][0:4]) > 2022 and int(row[0][5:7]) == 9)]
    return newData


def removeDirection(data):
    for i in range(len(data)-2):
        # print(data[i])
        # print(data[i][5])
        data[i].pop(5)
    print(data)


def test(data):
    for i in range(len(data)):
            if float(data['open'][i]) + 0.005 < float(data['close'][i]):
                # data['direction'][i] = 1
                data.loc[i, 'direction'] = 2
            elif float(data['open'][i]) - 0.005 > float(data['close'][i]):
                data.loc[i, 'direction'] = 0
            else:
                data.loc[i, 'direction'] = 1
    return data

