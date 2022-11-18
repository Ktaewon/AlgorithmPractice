import sys
import heapq
input = sys.stdin.readline

N = int(input())
heap = []
for _ in range(N):
    std_name, score = input().split()
    heapq.heappush(heap, (int(score), std_name))
for _ in range(N):
    print(heapq.heappop(heap)[1], end=' ')