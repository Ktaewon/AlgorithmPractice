# 문제
# N x M의 얼음 틀 (구멍 -> 0, 칸막이 -> 1)
# 구멍이 뚫여있는 부분끼리 상, 하, 좌, 우로 붙어 있는 경우 -> 서로 연결됨
# 생성되는 총 아이스크림 개수 구하기

# 풀이
# DFS를 이용해 풀 수 있다

def dfs(arr, i, j, visited, directions, N, M):
    visited[i][j] = True
    need_to_visits = []
    for d in directions:
        tx = i + d[0]
        ty = j + d[1]
        if tx >= 0 and tx < N and ty >= 0 and ty < M and arr[tx][ty] == '0':
            need_to_visits.append((tx, ty))
    for node in need_to_visits:
        if not visited[node[0]][node[1]]:
            dfs(arr, node[0], node[1], visited, directions, N, M)


def solution(N, M, arr):
    answer = 0
    # 상 하 좌 우 방향
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    # 방문 배열
    visited = [[False] * M for _ in range(N)]
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if visited[i][j] or arr[i][j] == '1':
                continue
            # DFS로 이어진 곳 모두 방문
            dfs(arr, i, j, visited, directions, N, M)
            answer += 1
    return answer

if __name__ == "__main__":
    N, M = map(int, input().split())
    arr = []
    for i in range(N):
        arr.append(input())
            
    print(solution(N, M, arr))
