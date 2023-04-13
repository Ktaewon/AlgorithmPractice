import sys

input = sys.stdin.readline

scores = [
        [100,90,98,88,65],
        [50,45,99,85,77],
        [47,88,95,80,67],
        [61,57,100,80,65],
        [24,90,94,75,65]
    ]

def score_to_grade(score):
    if (score >= 90):
        return "A"
    elif (score >= 80):
        return "B"
    elif (score >= 70):
        return "C"
    elif (score >= 50):
        return "D"
    return "F"

results = []
for i in range(len(scores)):
    min_score = scores[0][i]
    total_score = 0
    min_flag = False
    for j in range(len(scores)):
        if (i == j and min_score >= scores[j][i]):
            min_flag = True
            continue
        else:
            total_score += scores[j][i]
    if min_flag:
        results.append(total_score / (len(scores) - 1))
    else:
        results.append(total_score / len(scores))
grade_results = ""
for result in results:
    grade_results += score_to_grade(result)
    
print(grade_results)

