import sys
sys.setrecursionlimit(10**6)
class Graph:
    def __init__(self):
        self.graph = {}
    def addVertex(self, vertex):
        self.graph[vertex] = []
    def addEdge(self, startVertex, endVertex):
        self.graph[startVertex].append(endVertex)


def searchParent(graph, startVertex, parentArr):
    for s in graph.graph[startVertex]:
        if parentArr[s] == 0:
            parentArr[s] = startVertex
            parentArr= searchParent(graph, s, parentArr)
    return parentArr
            
# 노드의 개수
N = int(sys.stdin.readline())

# 그래프 선언
cGrpah = Graph()
parent = []

# vertex 추가
for i in range(N):
    cGrpah.addVertex(i + 1)
    parent.append(0)
parent.append(0)

# edge 추가
for i in range(N - 1):
    c1, c2 = map(int, sys.stdin.readline().split())
    cGrpah.addEdge(c1, c2)
    cGrpah.addEdge(c2, c1)

searchParent(cGrpah, 1, parent)
for data in parent[2:]:
    print(data)