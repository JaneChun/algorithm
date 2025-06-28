import heapq

def solution(operations):
    min_heap = []
    max_heap = []
    
    for op in operations:
        if op.startswith('I'):
            num = int(op[2:])
            heapq.heappush(min_heap, num)
            heapq.heappush(max_heap, -num)
        elif op == 'D 1' and len(max_heap):
            max_val = -heapq.heappop(max_heap)
            max_idx = min_heap.index(max_val)
            min_heap.pop(max_idx)
            heapq.heapify(min_heap)
        elif op == 'D -1' and len(min_heap):
            min_val = heapq.heappop(min_heap)
            min_idx = max_heap.index(-min_val)
            max_heap.pop(min_idx)
            heapq.heapify(max_heap)
            
    return [max(min_heap), min_heap[0]] if len(min_heap) else[0, 0]