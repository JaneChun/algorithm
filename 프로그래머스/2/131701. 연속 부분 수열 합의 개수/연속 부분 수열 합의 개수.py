def solution(elements):
    sum_set = set()
    
    # 길이별로 수열의 합 구하기
    for sub_len in range(1, len(elements) + 1): # 1, 2, 3, 4, 5
        extended_elements = elements + elements[0 : sub_len]
        
        for i in range(0, len(extended_elements)):
            sub_sum = extended_elements[i : i + sub_len]
            sum_set.add(sum(sub_sum))
            
    return len(sum_set)