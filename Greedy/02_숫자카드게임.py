import sys

input = sys.stdin.readline

# N행 M열
N, M = map(int, input().split())

arr = []
max_num = 0

for i in range(N):
    temp = min(list(map(int, input().split())))
    max_num = max(max_num, temp)
        
print(max_num)
