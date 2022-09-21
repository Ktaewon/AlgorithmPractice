import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()
first_big = arr[-1]
second_big = arr[-2]

result = 0
for i in range(1, M + 1):
    if i % (K + 1) == 0:
        result += second_big
    else:
        result += first_big

print(result)