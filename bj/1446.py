import sys

input = sys.stdin.readline

N, D = map(int, input().split())

short = []
dp = [0]

for _ in range(N):
    start, end, length = map(int, input().split())
    short.append([start, end, length])
short.sort(key=lambda x: x[1])

for i in range(1, D + 1):
    dp.append(dp[i - 1] + 1)
    for j in range(N):
        if short[j][1] > i:
            break
        elif short[j][1] == i:
            dp[i] = min(dp[i], dp[short[j][0]] + short[j][2])

print(dp[-1])