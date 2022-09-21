import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

def dijkstra(graph, x, shortest):
    # 시작 노드에서 해당 노드까지는 거리 0
    shortest[x] = 0
    q = []
    heapq.heappush(q, (0, x))
    while q: # 큐가 비어있지 않을 때
        # 최단 거리가 가장 짧은 노드 꺼내기
        dist, node = heapq.heappop(q)
        # 이미 처리한 노드(방문한 노드)일 경우 무시
        if shortest[node] < dist:
            continue
        # 해당 노드와 연결된 인접 노드 확인
        for k in graph[node]:
            # 해당 노드를 거쳐 다른 노드로 가는 거리가 더 짧을 경우
            if shortest[k] > dist + 1: # 해당 문제에서는 거리가 모두 1이므로 1을 더함 
                shortest[k] = dist + 1 # 최단 경로 업데이트
                heapq.heappush(q, (shortest[k], k)) # 큐에 삽입

#도시의 개수 N, 도로의 개수 M, 거리 정보 K, 출발 도시의 번호 X
N, M, K, X = map(int, input().split())

# 각 노드에 연결되어 있는 노드 담을 그래프
graph = [[] for j in range(N + 1)] 
# 출발 노드로부터 각 정점까지의 최단거리 담을 배열 초기화
shortest = [INF] * (N + 1)

# 모든 간선 정보 입력
for _ in range(M):
    n, m = map(int, input().split())
    graph[n].append(m)

# 다익스트라 수행
dijkstra(graph, X, shortest)
result = -1
# 최단 거리가 K인 노드 오름차순 출력
for i in range(N + 1):
    if shortest[i] == K:
        print(i)
        result = 1
# 결과가 없다면 -1 출력
if result == -1:
    print(result)