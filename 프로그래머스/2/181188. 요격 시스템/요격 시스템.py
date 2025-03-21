def solution(targets):
    count = 0
    targets.sort(key=lambda x: x[1]) # 끝점을 기준으로 정렬
    last_shoot_x = -1
    
    for s, e in targets:
        if s <= last_shoot_x: # 현재 미사일이 마지막 요격 지점에 속한다면
            continue
        else:
            count += 1
            last_shoot_x = e - 0.1
    
    return count