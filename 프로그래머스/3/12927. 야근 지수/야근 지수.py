import heapq

def solution(n, works):
    answer = 0
    max_heap = [-work for work in works]
    heapq.heapify(max_heap)
    
    for i in range(n):
        largest_work = heapq.heappop(max_heap)
        heapq.heappush(max_heap, min(0, largest_work + 1))
    
    return sum([i ** 2 for i in max_heap])