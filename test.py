import sys
input = sys.stdin.readline

N = int(input())
wine_list = [0] * N
dp = [0] * N
for i in range(N):
    wine_list[i] = int(input())

for i in range(N):
    if i == 0:
        dp[i] = wine_list[i]
    elif i == 1:
        dp[i] = dp[0] + wine_list[i]
    elif i == 2:
        dp[i] = max(dp[1], dp[0]+wine_list[i], wine_list[1] + wine_list[i])
    elif i >= 3:
        dp[i] = max((dp[i-3] + wine_list[i-1] + wine_list[i]), (dp[i-2] + wine_list[i]), dp[i-1])

print(max(dp))