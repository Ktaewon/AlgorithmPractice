import sys

T = int(sys.stdin.readline())

for i in range(T):
    N = int(sys.stdin.readline())
    scores = []
    maxPaperScore = 0
    maxInterviewScore = 0
    failer = 0
    successOnPaper = -1
    successOnInterview = -1
    for j in range(N):
        scores.append(list(map(int,sys.stdin.readline().split())))
        if maxPaperScore < scores[j][0]:
            maxPaperScore = scores[j][0]
            successOnPaper = j      
        if maxInterviewScore < scores[j][1]:
            maxInterviewScore = scores[j][1]
            successOnInterview = j
    for j in range(N):
        if scores[successOnPaper][1] > scores[j][1] and scores[successOnInterview][0] > scores[j][0]:
            print(j)
            failer += 1
        else:
            if scores[j][0] < maxPaperScore:
                maxPaperScore = scores[j][0]
                successOnPaper = j
            if scores[j][1] < maxInterviewScore:
                maxInterviewScore = scores[j][1]
                successOnInterview = j
    print(failer)
print(sorted(scores, key=lambda d: (-d[0], -d[1])))