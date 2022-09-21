import sys

input = sys.stdin.readline

def solution(orders, course):
    answer = []
    ordersCountDic = {}
    for order in orders:
        for o in order:
            if o in ordersCountDic:
                ordersCountDic[o] += 1
            else:
                ordersCountDic[o] = 1
    print(ordersCountDic)
    for c in course:
        temp = []

        answer.append(temp)
    return answer

orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
course = [2,3,4]
print(solution(orders, course))