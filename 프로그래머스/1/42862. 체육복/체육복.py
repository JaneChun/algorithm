def solution(n, lost, reserve):
    filtered_reserve = sorted([i for i in reserve if i not in lost])
    filtered_lost = sorted([i for i in lost if i not in reserve])
    
    answer = n - len(filtered_lost) 
    
    for l in filtered_lost:
        if l - 1 in filtered_reserve :
            filtered_reserve.remove(l - 1)
            answer += 1
            continue
            
        if l + 1 in filtered_reserve:
            filtered_reserve.remove(l + 1)
            answer += 1
            continue
    
    return answer