import sys

input = sys.stdin.readline

def visit(arr, visited, sx, sy, sd, direction):
    count = 1
    visited[sx][sy] = 1
    x = sx
    y = sy
    d = sd
    d_count = 0
    while True:
        if d_count == 4:
            tx = x + direction[(d - 2) % 4][0]
            ty = y + direction[(d - 2) % 4][1]
            if tx >= 0 and ty >= 0 and tx < N and ty < M and arr[tx][ty] != 1:
                x = tx
                y = ty
                if visited[x][y] != 1:
                    visited[x][y] = 1
                    count += 1
            else:
                break
            d_count = 0
        # 현재 방향의 왼쪽
        d = (d - 1) % 4
        d_count += 1
        tx = x + direction[d][0]
        ty = y + direction[d][1]
        if tx >= 0 and ty >= 0 and tx < N and ty < M and visited[tx][ty] != 1 and arr[tx][ty] != 1:
            count += 1
            d_count = 0
            visited[tx][ty] = 1
            x = tx
            y = ty
    return count

direction = (
    # 북 동 남 서
    (-1, 0), (0, 1), (1, 0), (0, -1)   
)
N, M = map(int, input().split())
# 시작점, 시작방향
sx, sy, sd = map(int, input().split())

arr = []
visited = []
for i in range(N):
    arr.append(list(map(int, input().split())))
    visited.append([0 for _ in range(M)])

print(visit(arr, visited, sx, sy, sd, direction))