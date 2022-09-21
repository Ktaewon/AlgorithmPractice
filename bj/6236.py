import sys

def binarySearch(startMoney, endMoney, useList, n, m):
    if n == 1:
        return useList[0]
    minPrice = endMoney
    while True:
        if startMoney > endMoney:
            return minPrice
        money = (startMoney + endMoney) // 2
        count = 1
        tempSum = 0
        flag = 0
        for dayMoney in useList:
            tempSum += dayMoney
            if money < tempSum:
                tempSum = dayMoney
                count += 1
            else:
                flag += 1
        if count < m:
            if flag > 0:
                if m - count <= flag:
                    count = m
        if count == m:
            minPrice = min(minPrice, money)
            endMoney = money - 1  
        elif count < m:
            endMoney = money - 1 
        else:
            startMoney = money + 1   


# N : 일, M : 번
N, M = map(int, sys.stdin.readline().split())

use = []
maxMoney = 0
totalSum = 0

for i in range(N):
    use.append(int(sys.stdin.readline()))
    maxMoney = max(use[i], maxMoney)
    totalSum += use[i]


print(binarySearch(maxMoney, totalSum, use, N, M))
    
#for i in range(N):
