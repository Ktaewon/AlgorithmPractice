import sys

def getTapeCount(leaks, n, l):
    lastTapeLoc = 0
    count = 0
    for i in range(n):
        if leaks[i] > lastTapeLoc:
            lastTapeLoc = leaks[i] - 0.5 + l
            count += 1
    return count

N, L = map(int, sys.stdin.readline().split())

locations = list(map(int, sys.stdin.readline().split()))
locations.sort()

print(getTapeCount(locations, N, L))
