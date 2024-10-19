def solution(priorities, location):
    order = 0
    priorities = [[p, i] for i, p in enumerate(priorities)]
    
    while len(priorities):
        [cur, i] = priorities.pop(0)
        
        if any(p > cur for [p, _] in priorities):
            priorities.append([cur, i])
        else:
            # 실행
            order += 1
            if i == location:
                return order