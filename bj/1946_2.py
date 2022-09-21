import sys

T = int(sys.stdin.readline())
success_list = []
for i in range(T):
    N = int(sys.stdin.readline())
    scores = []
    success = 1
    for j in range(N):
        scores.append(list(map(int,sys.stdin.readline().split())))
    scores.sort(key=lambda d: (d[0]))
    maxValue = scores[0][1]
    for j in range(1, N):
        if maxValue >= scores[j][1]:
            maxValue = scores[j][1]
            success += 1
    success_list.append(success)
    
for success in success_list:
    print(success)