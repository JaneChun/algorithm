def solution(diffs, times, limit):
    left = 1
    right = max(diffs)
    
    while left <= right:
        mid = (left + right) // 2
        
        if is_possible(diffs, times, limit, mid):
            right = mid - 1
        else:
            left = mid + 1
    
    return left

def is_possible(diffs, times, limit, level):
    total_time = 0
    
    for i in range(len(diffs)):
        diff = diffs[i]
        time_cur = times[i]
        time_prev = 0 if i == 0 else times[i - 1]
        
        # 풀 수 있는 문제
        if diff <= level:
            total_time += time_cur
        # 못 푸는 문제
        else:
            fail_count = diff - level
            total_time += fail_count * (time_cur + time_prev) + time_cur
        
    return total_time <= limit
    
    