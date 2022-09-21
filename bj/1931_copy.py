N = int(input());
data = []
result = []
count = 0
for i in range(N):
    d1, d2 = map(int, input().split())
    diff = d2 - d1
    data.append({'d1' : d1, 'd2': d2, 'diff' : diff})

data = sorted(data, key=lambda d: (d['d2'], d['diff']))
print(data)
last = 0
for d in data:
    flag = 0
    for r in result:
        # 이미 있는 시간 사이에 있는 경우
        if r['d1'] < d['d1'] and r['d2'] > d['d2']:
            flag = 1
            break
        # 왼쪽에서 겹치는 경우
        elif r['d1'] > d['d1'] and r['d1'] < d['d2']:
            flag = 1
            break
        # 오른쪽에서 겹치는 경우
        elif r['d2'] > d['d1'] and r['d2'] < d['d2']:
            flag = 1
            break
    if (flag == 0):
        count += 1
        result.append(d)
    flag = 0


print(count)