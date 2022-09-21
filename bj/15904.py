import sys


inputData = sys.stdin.readline()
indexU = -1
indexC1 = -1
indexP = -1
indexC2 = -1

indexU = inputData.find('U')
if indexU >= 0:
    indexC1 = inputData.find('C', indexU)
if indexC1 > 0:
    indexP = inputData.find('P' , indexC1)
if indexP > 0:
    indexC2 = inputData.find('C', indexP)
    print(indexC2)
if indexC2 > 0:
    print('I love UCPC')
else:
    print('I hate UCPC')