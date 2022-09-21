from sys import stdin
from collections import deque

#     북 북동 동 남동 남 남서 서 북서
dx = (-1, -1,  0,  1,  1,  1,  0, -1)
dy = ( 0,  1,  1,  1,  0, -1, -1, -1)

# 상어가 있는 곳으로부터 BFS하여 1씩 뻗어나간다.
def bfs(queue, area, n, m):
    max = 0
    while queue:
        x, y = queue.popleft()
        for i in range(8):
            X = x + dx[i]
            Y = y + dy[i]
            if (X < 0) or (Y < 0) or (X > n - 1) or (Y > m - 1):
                continue
            # 0이 아닌 곳은 다른 상어가 이미 지나간 곳이다
            if area[X][Y] == 0:
                area[X][Y] = area[x][y] + 1
                queue.append((X, Y))
            # 최대값 계산
            if max < area[X][Y]:
                max = area[X][Y]
    return max

N, M = map(int, stdin.readline().split())
area = []
queue = deque()

for i in range(N):
    area.append(list(map(int, stdin.readline().split())))
    for j in range(M):
        # 상어가 있는 곳의 좌표를 큐에 넣음
        if area[i][j] == 1:
            queue.append((i, j))
            
maxValue = 0

if queue:
    maxValue = bfs(queue, area, N, M) - 1
else:
    maxValue = max(N, M) 
print(maxValue)