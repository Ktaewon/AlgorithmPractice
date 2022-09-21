# two pointer
def solution(n, x, y):
    # sum
    sum_n = n*(n+1)//2
    # 
    if sum_n % (x + y) != 0:
        return (False, )
    else:
        div = sum_n // (x + y)
        ob_sum = div * x # 목표 합계
        if ob_sum <= n:
            return (True, ob_sum, ob_sum)
        if div > n:
            div = n // 2
        start = div
        end = div
        temp_sum = div
        while temp_sum != ob_sum:
            if temp_sum < ob_sum:
                if ob_sum - temp_sum >= end + 1:
                    if end == n:
                        start -= 1
                        temp_sum += start
                    else:
                        end += 1
                        temp_sum += end
                else:
                    if ob_sum - temp_sum > start - 1:
                        end += 1
                        temp_sum += end
                        temp_sum -= start
                        start += 1
                    else:
                        start -= 1
                        temp_sum += start
            else:
                if temp_sum - ob_sum >= end:
                    temp_sum -= end
                    end -= 1
                else:
                    if temp_sum - ob_sum < start:
                        start -= 1
                        temp_sum += start
                        temp_sum -= end
                        end -= 1
                    else:
                        temp_sum -= start
                        start += 1
        return (True, start, end)            
    

# T : the number of test cases
T = int(input())
answers = []

for i in range(T):
    # N : N positive integers (1,2,…,N)
    N, X, Y = map(int,input().split())
    answers.append(solution(N, X, Y))
    
for i in range(T):
    if answers[i][0] == False:
        result = "IMPOSSIBLE"
        print("Case #{}: {}".format(i + 1, result))
    elif answers[i][0] == True:
        result = "POSSIBLE"
        print("Case #{}: {}".format(i + 1, result))
        if answers[i][1] == answers[i][2]:
            print("1\n{}".format(answers[i][1]))
        else:
            print("{}".format(answers[i][2] - answers[i][1] + 1))
            for i in range(answers[i][1], answers[i][2] + 1):
                print(i, end=' ')
            print()