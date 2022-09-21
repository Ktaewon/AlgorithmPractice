import sys
from collections import deque

def bfs(area, start, visited, distance, n, m):
    x, y = start
    queue = deque([start])
    visited[x][y] = True
    count = 0
    max = 0
    
    while queue:
        print(queue)
        flag = 0
        x, y = queue.popleft()
        # 북
        X = x - 1
        Y = y
        if (X > 0):
            if area[X][Y] == 0 and visited[X][Y] == False:
                visited[X][Y] = True
                queue.append((X, Y))
            elif area[X][Y] == 1:
                flag = 1 
        # 북동
        X = x - 1
        Y = y + 1
        if (X > 0) and (Y < m):
            if area[X][Y] == 0 and visited[X][Y] == False:
                visited[X][Y] = True
                queue.append((X, Y))
            else:
                flag = 1 
        # 동
        X = x
        Y = y + 1
        if (Y < m):
            if area[X][Y] == 0 and visited[X][Y] == False:
                visited[X][Y] = True
                queue.append((X, Y))
            else:
                flag = 1 
        # 남동
        X = x + 1
        Y = y + 1
        if (X < n) and (Y < m):
            if area[X][Y] == 0 and visited[X][Y] == False:
                visited[X][Y] = True
                queue.append((X, Y))
            else:
                flag = 1 
        # 남
        X = x + 1
        Y = y
        if (X < n):
            if area[X][Y] == 0 and visited[X][Y] == False:
                visited[X][Y] = True
                queue.append((X, Y))
            else:
                flag = 1 
        # 남서
        X = x + 1
        Y = y - 1
        if (X < n) and (Y > 0):
            if area[X][Y] == 0 and visited[X][Y] == False:
                visited[X][Y] = True
                queue.append((X, Y))
            else:
                flag = 1 
        # 서
        X = x
        Y = y - 1
        if (Y > 0):
            if area[X][Y] == 0 and visited[X][Y] == False:
                visited[X][Y] = True
                queue.append((X, Y))
            else:
                flag = 1 
        # 북서
        X = x - 1
        Y = y - 1
        if (X > 0) and (Y > 0):
            if area[X][Y] == 0 and visited[X][Y] == False:
                visited[X][Y] = True
                queue.append((X, Y))
            else:
                flag = 1 
        if flag == 0:
            count = 1
        else:
            count += 1
            if max < count:
                max = count
    return max

N, M = map(int, sys.stdin.readline().split())
area = []
visited = []
distance = []

for i in range(N):
    area.append(list(map(int, sys.stdin.readline().split())))
    visited.append([])
    distance.append([])
    for j in range(M):
        visited[-1].append(False)
        distance[-1].append(0)
print(area)
print(bfs(area, (0, 0), visited, distance, N, M))