def solution(stones, k):
    answer = 0
    left = 1
    right = max(stones)
    
    while left <= right:
        mid = (left + right) // 2
        # print(left, right, ' -> ',mid)
        
        if is_possible(stones, mid, k):
            answer = mid
            left = mid + 1
        else:
            right = mid - 1        
    
    return answer

def is_possible(stones, mid, k):
    count = 0
    
    for s in stones:
        if s < mid:
            count += 1
        else:
            count = 0
            
        if count >= k:
            return False
    
    return True 