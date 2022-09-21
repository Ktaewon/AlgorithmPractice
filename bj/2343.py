import sys

def check(key, videoList, m):
    count = 1
    tempSum = 0
    for video in videoList:
        tempSum += video
        if key < tempSum:
            tempSum = video
            count += 1
    return count > m

def binarySearch(sb, eb, videoList, n, m):
    if n == 1:
        return videoList[0]
    while sb <= eb:
        bluray = (sb + eb) // 2
        if check(bluray, videoList, m):
            sb = bluray + 1 
        else:
            eb = bluray - 1
    return sb


# N : 비디오 개수, M : 블루레이 개수
N, M = map(int, sys.stdin.readline().split())

video = list(map(int,sys.stdin.readline().split()))

print(binarySearch(max(video), sum(video), video, N, M))
