def solution(brown, yellow): # 10, 2
    total_surface = brown + yellow # 12
    
    # total_surface의 약수를 구한다.
    possible_matches = [] # [[12, 1], [6, 2], [4, 3]]
    for i in range(1, int(total_surface ** 0.5) + 1):
        if total_surface % i == 0:
            possible_matches.append([total_surface // i, i])
    
    for w, h in possible_matches:
        if (w - 2) * (h - 2) == yellow:
            return [w, h]
    