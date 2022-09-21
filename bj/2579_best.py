import sys

def operateDP(n):
    scores = [0]
    dp = [0]
    for _ in range(N):
        scores.append(int(input()))

    dp.append(scores[1])

    if N > 1:
        dp.append(dp[1] + scores[2])

    for i in range(3, N + 1):
        dp.append(max(dp[i - 2] + scores[i], dp[i - 3] + scores[i - 1] + scores[i]))
    return dp[n]

input = sys.stdin.readline

N = int(input())

print(operateDP(N))