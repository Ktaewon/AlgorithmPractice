from statistics import mean
import sys
import math
import decimal

N, K = map(int, sys.stdin.readline().split())

prefer = list(map(decimal.Decimal, sys.stdin.readline().split()))
perfer_sqr = [x ** 2 for x in prefer]

minVariance = sys.maxsize
"""
for k in range(K, N + 1):
    print(k)
    for i in range(N - k + 1):
        meanPrefer = sum(prefer[i:i + k]) / k
        sqrMean = sum(perfer_sqr[i:i + k]) / k
        variance = sqrMean - meanPrefer ** 2
        print(meanPrefer, sqrMean ** 2, variance)
        print('{} ~ {}, 분산: {}'.format(i, i + k - 1, variance))
        print(math.sqrt(variance))
        if variance < minVariance:
            minVariance = variance
"""

for i in range(N - K + 1):
    sumPrefer = sum(prefer[i:i + K - 1])
    sumPreferSqr = sum(perfer_sqr[i:i + K - 1])
    for j in range(N - K + 1 - i):
        print(i, i + K - 1, j)
        sumPrefer += prefer[i + K + j - 1]
        sumPreferSqr += perfer_sqr[i + K + j - 1]
        meanPrefer = sumPrefer / (K + j)
        sqrMean = sumPreferSqr / (K + j)
        variance = sqrMean - meanPrefer ** 2
        if variance < minVariance:
            minVariance = variance

print(math.sqrt(minVariance))