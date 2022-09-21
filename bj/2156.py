# 백준 2156번 포도주 시식
import sys

def findMaxScores(scores, max_scores, N):
    scores.append(0)
    max_scores.append(0)
    # 점수 입력
    for _ in range(N):
        score = int(sys.stdin.readline())
        scores.append(score)
        max_scores.append(score)
    if N == 1:
        return scores[1]
    check = [0] * (N + 1)
    max_scores[2] += max_scores[1]
    check[2] = -1
    
    for i in range(3, N + 1):
        if check[i - 1] != -1:
            if max_scores[i - 2] + scores[i] >= max_scores[i - 1] + scores[i]:
                max_scores[i] = max_scores[i - 2] + scores[i]
            else:
                max_scores[i] = max_scores[i - 1] + scores[i]
                check[i] = -1
        else:
            if i - 3 == 0:
                if max_scores[i - 3] + scores[i - 1] + scores[i] <= max_scores[i - 3] + scores[i - 2] + scores[i]:
                    max_scores[i] = max_scores[i - 3] + scores[i - 2] + scores[i]
                else:
                    max_scores[i] = max_scores[i - 3] + scores[i - 1] + scores[i]
                    check[i] = -1
            else:
                temp = max(max_scores[1: i - 2])
                if temp + scores[i - 1] + scores[i] >= max_scores[i - 2] + scores[i]:
                    max_scores[i] = temp + scores[i - 1] + scores[i]
                    check[i] = -1
                else:
                    max_scores[i] = max_scores[i - 2] + scores[i]

    return max(max_scores)

# 와인의 수
N = int(sys.stdin.readline())
# 와인 점수 리스트
scores = []
max_scores = []

print(findMaxScores(scores, max_scores, N))
