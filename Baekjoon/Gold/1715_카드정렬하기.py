import sys
from heapq import heappush, heappop

n = int(sys.stdin.readline())
heap = []
for _ in range(n):
    heappush(heap, int(sys.stdin.readline()))

cnt_compare = 0
while len(heap) != 1:
    a, b = heappop(heap), heappop(heap)
    cnt_compare += (a+b)
    heappush(heap, a+b)

print(cnt_compare)
