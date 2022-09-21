from statistics import variance
import sys

N, K = map(int, sys.stdin.readline().split())

prefer = list(map(int, sys.stdin.readline().split()))
perfer_sqr = [x ** 2 for x in prefer]

minVariance = 10**12

for i in range(N - K + 1):
    sumPrefer = sum(prefer[i:i + K - 1])
    #sumPreferSqr = sum(perfer_sqr[i:i + K - 1])
    for j in range(N - K + 1 - i):
        sumPrefer += prefer[i + K + j - 1]
        #sumPreferSqr += perfer_sqr[i + K + j - 1]
        print(sumPrefer)
        m = sumPrefer / (K + j)
        temp = 0
        for k in range(i , i + K + j):
            temp += (prefer[k] - m) ** 2
        variance = temp / (K + j)
        minVariance = min(minVariance, variance)    
        #minVariance = min(minVariance, (sumPreferSqr / (K + j)) - (sumPrefer / (K + j)) ** 2)
print(minVariance)
print(minVariance ** 0.5)
print(9000000000000 / 10)