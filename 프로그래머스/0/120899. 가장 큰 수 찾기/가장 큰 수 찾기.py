def solution(array):
    answer = []
    max_value = max(array)
    
    for idx, num in enumerate(array):
        if num == max_value:
            answer.extend([num, idx])
        
    return answer