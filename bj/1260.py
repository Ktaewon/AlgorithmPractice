import sys
from collections import deque
input = sys.stdin.readline

class Graph:
    def __init__(self):
        self.graph = {}
    def addVertex(self, vertex):
        self.graph[vertex] = []
    def addEdge(self, vertex1, vertex2):
        if vertex2 not in self.graph[vertex1]:
            self.graph[vertex1].append(vertex2)
        if vertex1 not in self.graph[vertex2]:
            self.graph[vertex2].append(vertex1)
    def DFS_iterated(self, startVertex):
        visited = []
        stack = deque()
        stack.append(startVertex)
        while stack:
            node = stack.pop()
            if node not in visited:
                visited.append(node)
                stack.extend(self.graph[node])
        return visited
    def DFS_recursion(self, startVertex, visited = []):
        visited.append(startVertex)
        for node in self.graph[startVertex]:
            if node not in visited:
                self.DFS_recursion(node, visited)
        return visited
    def BFS_iterated(self, startVertex):
        visited = []
        queue = deque()
        queue.append(startVertex)
        while queue:
            node = queue.popleft()
            if node not in visited:
                visited.append(node)
                queue.extend(self.graph[node])
        return visited


# 정점의 개수 N(1 ≤ N ≤ 1,000), 
# 간선의 개수 M(1 ≤ M ≤ 10,000), 
# 탐색을 시작할 정점의 번호 V
N, M, V = map(int, input().split())

graph = Graph()
for i in range(1, N + 1):
    graph.addVertex(i)

for _ in range(M):
    v1, v2 = map(int, input().split())
    graph.addEdge(v1, v2)

for i in range(1, N + 1):
    graph.graph[i].sort()
    
#print(graph.DFS_iterated(startVertex=V))
print(*graph.DFS_recursion(startVertex=V), sep = ' ')
print(*graph.BFS_iterated(startVertex=V), sep = ' ')