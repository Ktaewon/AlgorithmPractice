import sys

def totalSum(loc, locations):
    totalSum = 0
    for location in locations:
        totalSum += abs(loc-location)
    return totalSum
def findPoleLocation(locations, n):
    poleLocation = locations[n // 2]
    if poleLocation - 1 <= 0 or poleLocation + 1 > locations[-1]:
        return poleLocation
    startSum = totalSum(poleLocation, locations)
    left = totalSum(poleLocation - 1, locations)
    right = totalSum(poleLocation + 1, locations)
    flag = 0
    minSum = 0
    if startSum >= left:
        flag = -1
        poleLocation -= 1
        minSum = left
    elif startSum <= right:
        return poleLocation
    elif startSum > right:
        flag = 1
        poleLocation += 1
        minSum = right

    while True:
        sumData = totalSum(poleLocation + flag, locations)
        if minSum >= sumData:
            if flag == 1:
                return poleLocation
            minSum = sumData
            poleLocation += flag
        else:
            return poleLocation

# 집의 수
N = int(sys.stdin.readline())

locations = list(map(int, sys.stdin.readline().split()))
locations.sort()

print(findPoleLocation(locations, N))