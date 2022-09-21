import sys

input = sys.stdin.readline

N, K = map(int, input().split())

count = 0

if K > N:
    count = N - 1
else:
    while N >= K:
        if N % K == 0:
            N = N // K
        else:
            N -= 1
        count += 1
    if N > 1:
        count += (N - 1)
print(count)