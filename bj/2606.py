import sys

class Graph:
    def __init__(self):
        self.graph = {}
    def addVertex(self, vertex):
        self.graph[vertex] = []
    def addEdge(self, startVertex, endVertex):
        self.graph[startVertex].append(endVertex)

def searchInfection(graph, startVertex, visited, count):
    visited[startVertex] = 1
    count += 1
    for s in graph.graph[startVertex]:
        if visited[s] != 1:
            visited, count = searchInfection(graph, s, visited, count)
    return visited, count
            
# 컴퓨터의 수
N = int(sys.stdin.readline())

# 그래프 선언
cGrpah = Graph()
visited = []

# vertex 추가
for i in range(N):
    cGrpah.addVertex(i + 1)
    visited.append(0)
visited.append(0)

# 연결된 컴퓨터 쌍 수
M = int(sys.stdin.readline())

# edge 추가
for i in range(M):
    c1, c2 = map(int, sys.stdin.readline().split())
    cGrpah.addEdge(c1, c2)
    cGrpah.addEdge(c2, c1)
    
# 검색
count = 0
visited, count = searchInfection(cGrpah, 1, visited, count)


# 방문한 노드 개수
print(count - 1)