import sys

N = int(sys.stdin.readline())
score = []

for i in range(N):
    score.append(int(sys.stdin.readline()))

count = 0
#last = score[-1]
for i in range(N - 2, -1, -1):
    if score[i + 1] <= score[i]:
        diff = score[i] - score[i + 1] + 1
        count += diff
        score[i] = score[i] - diff
    else:
        score[i] = score[i]

print(count)