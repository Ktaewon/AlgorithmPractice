#18114번 블랙프라이데이
import sys

def binarySearch(start, end, c, weights):
    while start <= end:
        mid = (start + end) // 2
        if weights[mid] == c:
            return mid
        if weights[mid] < c:
            start = mid + 1
        else:
            end = mid - 1
    return -1

def event(n, c, weights):
    for i in range(n - 1, -1, -1):
        if c == weights[i]:
            return True
        elif c < weights[i]:
            continue
        weightSum = 0
        j = i
        count = 0
        while j >= 0:
            if c >= weightSum + weights[j]:
                count += 1
                if count > 3:
                    break
                weightSum += weights[j]
                if c == weightSum:
                    return True
                else:
                    if count >= 3:
                        break
                    key = c - weightSum
                    if key < weights[j]:
                        index = binarySearch(0, j - 1, key, weights)
                        if index >= 0:
                            return True
            j -= 1
    return False

# N : 물건 개수, C : 무게
N, C = map(int, sys.stdin.readline().split())

# N개의 물건의 무게들
weights = list(map(int, sys.stdin.readline().split()))
weights.sort()

if event(N, C, weights):
    print(1)
else:
    print(0)