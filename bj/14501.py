# 14501번 퇴사
# 파이썬
# 김태원

import sys

input = sys.stdin.readline

N = int(input())
consulting = [(0, 0)]
dp = [0]

for _ in range(N):
    consulting.append(tuple(map(int, input().split())))
    
for i in range(1, N + 1):
    # 당일 상담 불가능
    if consulting[i][0] > 1:
        dp.append(dp[i - 1])
    # 당일 상담 가능
    else:
        dp.append(dp[i - 1] + consulting[i][1])
    for j in range(i - 1, 0, -1):
        if consulting[j][0] + (j - 1) == i:
            dp[i] = max(dp[i], consulting[j][1] + dp[j - 1])
        
print(dp[N])
