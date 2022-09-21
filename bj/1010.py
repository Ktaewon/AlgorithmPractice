# 1010번 다리놓기
# 파이썬 김태원

import sys
input = sys.stdin.readline

# 테스트 케이스 수
T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    if N == M:
        print(1)
    arr = [0]
    for i in range(M):
        arr.append(i + 1)
    for i in range(2, N + 1):
        new_arr = []
        for j in range(i, M + 1):
            new_arr.append(sum(arr[i - 1:j]))
        arr[i:] = new_arr
    print(arr[-1])
    