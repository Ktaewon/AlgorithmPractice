import sys
import operator

N = int(sys.stdin.readline())
numList = []

def calculate(arr, n):
    arr.sort()
    dictArr = {num: 0 for num in arr}
    resultDir = {}
    totalSum = 0
    for i in range(N):
        totalSum += arr[i]
        dictArr[arr[i]] += 1
    resultDir['mean'] = totalSum / n
    resultDir['median'] = arr[n // 2]
    resultDir['range'] = arr[-1] - arr[0]
    sdict = sorted(dictArr.items(), key=operator.itemgetter(1), reverse=True)
    if len(sdict) == 1:
        resultDir['mode'] = sdict[0][0]
    else:
        if sdict[0][1] > sdict[1][1]:
            resultDir['mode'] = sdict[0][0]
        else:
            resultDir['mode'] = sdict[1][0]
    return resultDir

for i in range(N):
    numList.append(int(sys.stdin.readline()))

result = calculate(numList, N)
print(round(result['mean']))
print(result['median'])
print(result['mode'])
print(result['range'])