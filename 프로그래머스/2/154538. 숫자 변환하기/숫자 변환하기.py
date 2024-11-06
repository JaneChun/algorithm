from collections import deque

def solution(x, y, n):
    queue = deque([(x, 0)])
    visited = set([x])
    
    while queue:
        cur_sum, cur_cnt = queue.popleft()
        
        if cur_sum == y:
            return cur_cnt
        
        # 3가지 연산 수행
        for next_sum in (cur_sum + n, cur_sum * 2, cur_sum * 3):
            if next_sum <= y and next_sum not in visited:
                queue.append((next_sum, cur_cnt + 1))
                visited.add(next_sum)
        
    return -1