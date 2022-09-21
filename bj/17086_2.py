import sys
from collections import deque
import copy

dx = [0, 1, 1, 1, 0, -1, -1, -1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]


def bfs(area, start, visited, distance, n, m):
    x, y = start
    queue = deque([start])
    visited[x][y] = True
    max = 0
    while queue:
        x, y = queue.popleft()
        for i in range(8):
            X = x + dx[i]
            Y = y + dy[i]
            if (X < 0) or (Y < 0) or (X > n - 1) or (Y > m - 1):
                continue
            if area[X][Y] == 0 and visited[X][Y] == False:
                visited[X][Y] = True
                if distance[X][Y] > distance[x][y] + 1 or distance[X][Y] == 0:
                    distance[X][Y] = distance[x][y] + 1
                if max < distance[X][Y]:
                    max = distance[X][Y]
                queue.append((X, Y))
    return max 

N, M = map(int, sys.stdin.readline().split())
area = []
visited = []
distance = []
queue = deque()

for i in range(N):
    area.append(list(map(int, sys.stdin.readline().split())))
    visited.append([])
    distance.append([])
    for j in range(M):
        if area[i][j] == 1:
            queue.append((i, j))
        visited[i].append(False)
        distance[i].append(0)

if queue:
    while queue:
        visited_t = copy.deepcopy(visited)
        shark = queue.popleft()
        maxValue = bfs(area, shark, visited_t, distance, N, M)
    print(maxValue)
else:
    print(max(N, M))

# for i in range(N):
#     for j in range(M):
#         if area[i][j] == 1:
#             visited_t = copy.deepcopy(visited)
#             maxValue = bfs(area, (i, j), visited_t, distance, N, M)
#             sharkExist = 1
# if sharkExist == 0:
#     print(max(N, M))
# else:
#     print(maxValue)
