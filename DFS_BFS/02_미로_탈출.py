# 문제)
# N x M 크기의 미로
# 여러 마리의 괴물이 존재하고, 피해야 한다
# 최초 위치 (1, 1)
# 미로 출구 (N, M)
# 괴물 있는 부분 -> 0, 괴물 없는 부분 -> 1
# 탈출을 위해 움직여햐하는 최소 칸의 개수 구하기(시작 칸, 마지막 칸 포함)

# 풀이)
# BFS를 이용하여 해결할 수 있다.
from collections import deque

def bfs(i, j, directions, arr, N, M):
    queue = deque()
    queue.append((i, j))
    # 큐가 빌 때 까지
    while queue:
        x, y = queue.popleft()
        for d in directions:
            tx = x + d[0]
            ty = y + d[1]
            if tx >= 0 and ty >= 0 and tx < N and ty < M and arr[tx][ty] != 0:
                if arr[tx][ty] == 1:
                    arr[tx][ty] = arr[x][y] + 1
                    queue.append((tx, ty))
    return arr       
                
def solution(N, M, arr):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    arr = bfs(0, 0, directions, arr, N, M)
    return arr[N - 1][M - 1]

if __name__ == "__main__":
    N, M = map(int, input().split())
    arr = []
    for i in range(N):
        arr.append(list(map(int, input())))
            
    print(solution(N, M, arr))
