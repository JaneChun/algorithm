import sys
import heapq

n = int(sys.stdin.readline())
min_heap = []

for _ in range(n):
    x = int(sys.stdin.readline())

    if x != 0:
        heapq.heappush(min_heap, x)
    else:
        if min_heap:
            print(heapq.heappop(min_heap))
        else:
            print(0)