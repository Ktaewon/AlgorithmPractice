import sys
from collections import deque

class Graph:
    def __init__(self):
        self.graph = {}
    def addVertex(self, vertex):
        self.graph[vertex] = []
    def addEdge(self, startVertex, endVertex):
        self.graph[startVertex].append(endVertex)

def bfs(graph, start, end, visited, distance):
    visited[start] = True
    distance[start] += 1
    queue = deque([start])
    while queue:
        vertex = queue.popleft()
        for v in graph[vertex]:
            if visited[v] == False:
                visited[v] = True
                distance[v] = distance[vertex] + 1
                if v == end:
                    return distance[v]
                queue.append(v)


        
N, M = map(int, sys.stdin.readline().split())
maze = []

mazeGraph = Graph()
visited = []
distance = []
for i in range(N * M): 
    mazeGraph.addVertex(i)
    visited.append(False)
    distance.append(0)

for i in range(N):
    maze.append(list(map(int, list(sys.stdin.readline().strip()))))

index = 0
for i in range(N):
    for j in range(M):
        if maze[i][j] != 0:
            if j != M - 1:
                if maze[i][j + 1] == 1:
                    mazeGraph.addEdge(index, index + 1)
                    mazeGraph.addEdge(index + 1, index)
            if i != N - 1:
                # 아래
                if maze[i + 1][j] == 1:
                    mazeGraph.addEdge(index, index + M)
                    mazeGraph.addEdge(index + M, index)
        index += 1

print(bfs(mazeGraph.graph, 0, N * M - 1, visited, distance))