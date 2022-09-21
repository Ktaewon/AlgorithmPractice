N = int(input());
data = []
timeTable = [0 for i in range(25)]
count = 0
for i in range(N):
    d1, d2 = map(int, input().split())
    diff = d2 - d1
    data.append({'d1' : d1, 'd2': d2, 'diff' : diff})

data = sorted(data, key=lambda d: d['diff'])
print(data)
for d in data:
    if d['diff'] == 0 and timeTable[d['d1']] != 1:
        print("같아")
        count += 1
    elif timeTable[d['d1'] + 1] != 1 and timeTable[d['d2'] - 1] != 1:
        print(d)
        for i in range(d['d1'], d['d2'] + 1):
            timeTable[i] = 1
        print(timeTable)
        count += 1
print(timeTable)
print(count)