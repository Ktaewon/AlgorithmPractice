import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()
first_big = arr[-1]
second_big = arr[-2]

count = (M // (K + 1)) * K
count += (M % (K + 1))

result = first_big * count
result += second_big * (M - count)

print(result)