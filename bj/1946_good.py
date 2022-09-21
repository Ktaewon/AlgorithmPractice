import sys
def solve1946(t):
    for i in range(t):
        N = int(sys.stdin.readline())
        scores = [0] * (N + 1)
        success = 1
        for j in range(N):
            dscore, iscore = map(int,sys.stdin.readline().split())
            scores[dscore] = iscore
        maxValue = scores[1]
        for j in range(2, N + 1):
            if maxValue >= scores[j]:
                maxValue = scores[j]
                success += 1
        print(success)
        
solve1946(int(sys.stdin.readline()))
