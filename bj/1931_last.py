import sys

# 회의의 수 N
N = int(sys.stdin.readline());
data = [] # 입력받을 시간 담을 배열
count = 0 # 횟수의 개수
# 회의 시작, 끝시간 입력
for i in range(N):
    d1, d2 = map(int, sys.stdin.readline().split())
    data.append({'d1' : d1, 'd2': d2})
# 끝시간 -> 시작시간 순으로 정렬
# 끝시간으로 정렬하게 되면, 
data = sorted(data, key=lambda d: (d['d2'], d['d1']))

last = 0 # 제일 마지막 값
for d in data:
    # 마지막 값과 비교해서 새로 들어오는 값이 더 크게 같을 때만 더함
    if last <= d['d1']: 
        count += 1
        last = d['d2']

print(count)