def solution(topping):
    answer = 0
    front_set = set()
    back_dict = {}
    
    for t in topping:
        back_dict[t] = back_dict.get(t, 0) + 1
    
    for t in topping:
        front_set.add(t) # 앞 부분에 토핑 추가
        back_dict[t] -= 1 # 뒤 부분의 토핑 개수 감소
    
        if back_dict[t] == 0: # 개수가 0이 되면 키를 삭제
            del back_dict[t]
            
        if len(front_set) == len(back_dict):
            answer += 1
    
    return answer