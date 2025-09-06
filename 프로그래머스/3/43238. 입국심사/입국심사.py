def solution(n, times):
    left = 1
    right = n * max(times)
    
    times.sort()
    
    while left <= right:
        mid = (left + right) // 2
        
        # mid분 안에 가능한지 체크
        total_can_handle = 0
        for t in times:
            one_can_handle = mid // t
            total_can_handle += one_can_handle
                
        if total_can_handle < n:
            left = mid + 1
        else:
            right = mid - 1
    
    return left