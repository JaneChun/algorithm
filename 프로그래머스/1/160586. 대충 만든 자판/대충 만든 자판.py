def solution(keymap, targets):
    answer = []
    
    for target in targets: # ABCD
        total = 0
        for char in target: # A
            cases = [keys.index(char) + 1 for keys in keymap if char in keys] # [2, 1]
            if cases: 
                total += min(cases)
            else:
                total = -1 # 문자가 없는 경우
                break
        answer.append(total)
        
    return answer