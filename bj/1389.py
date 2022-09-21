import sys

input = sys.stdin.readline
INF = int(1e9)

def dfs(i, arr, answer, visited, origin):
    for p in range(N):
        if arr[i][p] == 1:
            if p not in visited:
                visited.add(p)
                answer[origin][p] = 1
                existsPath(p, arr, answer, visited, origin)
    return visited

# 유저의 수 N (2 ≤ N ≤ 100)
# 친구 관계의 수 M (1 ≤ M ≤ 5,000)
N, M = map(int, input().split())
friends = [[INF] * (N + 1) for _ in range(N)]

for _ in range(M):
    person1, person2 = map(int, input().split())
    friends[person1].append(person2)
    friends[person2].append(person1)
