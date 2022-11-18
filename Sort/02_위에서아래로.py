import sys
import heapq
input = sys.stdin.readline

N = int(input())
heap = []
for _ in range(N):
    num = int(input())
    heapq.heappush(heap, (-num, num))
for _ in range(N):
    print(heapq.heappop(heap)[1], end=' ')