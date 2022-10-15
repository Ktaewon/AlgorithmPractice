# DFS (Depth-Frist-Search, 깊이 우선 탐색)
# * 그래프에서 깊은 부분을 우선적으로 탐색하는 기법
# * 한 번 탐색할 때 최대한 깊숙이 들어가게 된다
# * O(N)의 탐색 시간을 가진다
#   1. 탐색 시작 노드를 스택에 삽입 & 방문 처리
#   2. 스택의 최상단 노드를 확인한다
#       1) 방문하지 않은 인접 노드가 있으면, 해당 인접 노드를 스택에 넣는다
#       2) 방문하지 않은 인접 노드가 없다면, 스택에서 최상단 노드를 꺼낸다
#   3. 2번의 과정을 더 이상 수행할 수 없을 때 까지 반복한다(스택이 빌 때 까지)
# * 반복문(iteration), 재귀(recursion) 모두 구현 가능하다
# * js의 경우 호출 스택의 Maximum Size가 브라우저 마다 다르고 매우 
#   작은 경우가 많기 때문에 반복문으로 구현하게 된다.

# 재귀적 구현
# 호출 스택이 너무 깊어진다면,
#   * import sys 
#   * sys.setrecusionlimit(...)
# 를 통해 늘려줄 수 있다.
def dfs(graph, v, visited):
    # 현재 노드를 방문 처리
    visited[v] = True
    print(v, end='')
    for i in graph[v]:
        if not visited[v]:
            dfs(graph, v, visited)

# 반복문 구현
# * stack으로 list를 사용해도 되지만,
#   삽입, 삭제의 조금의 효율성을 위해 deque를 사용했다.
from collections import deque
def dfs_iterated(self, startVertex, visited):
        visited[startVertex] = True
        stack = deque()
        stack.append(startVertex)
        while stack:
            node = stack.pop()
            if not visited[node]:
                visited[node] = True
                stack.extend(self.graph[node])
        return visited

visited = [False] * 9