import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline
        
def existsPath(i, j, arr, visited):
    result = 0
    for p in range(N):
        if arr[i][p] == 1:
            if p == j:
                return 1
            if p not in visited:
                visited.add(p)
                result = existsPath(p, j, arr, visited)
                if result == 1:
                    break
    return result

N = int(input())

arr = []
answer = []

for _ in range(N):
    arr.append(list(map(int, input().split())))
    answer.append([0] * N)
for i in range(N):
    for j in range(N):
        visited = set()
        visited.add(i)
        temp = existsPath(i, j, arr, visited)
        print(temp, end=' ')
        answer[i][j] = temp
    print()

