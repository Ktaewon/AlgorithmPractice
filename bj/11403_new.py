import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline
        
def existsPath(i, arr, answer, visited, origin):
    for p in range(N):
        if arr[i][p] == 1:
            if p not in visited:
                visited.add(p)
                answer[origin][p] = 1
                existsPath(p, arr, answer, visited, origin)
    return visited
N = int(input())

arr = []
answer = []

for _ in range(N):
    arr.append(list(map(int, input().split())))
    answer.append([0] * N)

for i in range(N):
    visited = set()
    existsPath(i, arr, answer, visited, i)
    for a in answer[i]:
        print(a, end=' ')
    print()

