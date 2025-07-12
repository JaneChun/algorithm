def solution(routes):
    answer = 0
    routes.sort(key=lambda x: (x[1], x[0]))
    
    loc = -float('inf') # -inf -> 15
    for s, e in routes: # -20, -15 -> -18, -13 -> -14, -5 -> -5, -3
        if loc < s:
            answer += 1
            loc = e
        
    return answer