def solution(babbling):
    answer = 0
    can = ["aya", "ye", "woo", "ma"]
    
    for babb in babbling:
        for c in can:
            if c * 2 not in babb:
                babb = babb.replace(c, ' ')
    
        if babb.isspace():
            answer += 1
        
    return answer