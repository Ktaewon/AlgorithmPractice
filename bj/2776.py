import sys

def binarySearch(arr, x):
    start = 0
    end = len(arr) - 1
    while True:
        if start > end:
            return -1
        index = (start + end) // 2
        if arr[index] < x:
            start = index + 1
        elif arr[index] > x:
            end = index - 1
        else:
            return index
            
            
    
# 테스트 케이스 개수
T = int(sys.stdin.readline())

for i in range(T):
    # 수첩1 정수 개수
    N = int(sys.stdin.readline())
    original = list(map(int, sys.stdin.readline().split()))
    original.sort()
    # 수첩2 정수 개수
    M = int(sys.stdin.readline())
    new = list(map(int, sys.stdin.readline().split()))

    for num in new:
        if binarySearch(original, num) >= 0:
            print(1)
        else:
            print(0)