def dfs(graph, v, visited):
    # 현재 노드를 방문 처리
    visited[v] = True
    print(v, end='')
    for i in graph[v]:
        if not visited[v]:
            dfs(graph, v, visited)

visited = [False] * 9