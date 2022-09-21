import sys
input = sys.stdin.readline
        
def existsPath(i, graph, answer, visited, origin):
    for p in graph[i]:
        if p not in visited:
            visited.add(p)
            answer[origin][p] = 1
            existsPath(p, graph, answer, visited, origin)
    return visited
N = int(input())

graph = []
answer = []

for i in range(N):
    graph.append([])
    tempList = list(map(int, input().split()))
    for j in range(N):
        if tempList[j] == 1:
            graph[i].append(j)
    answer.append([0] * N)

for i in range(N):
    visited = set()
    existsPath(i, graph, answer, visited, i)
    for a in answer[i]:
        print(a, end=' ')
    print()

