def solution(n, build_frame):
    answer = []
    pillars = set()
    beams = set()
    
    def can_build_pillar(x, y):
        # 바닥 위에 있거나
        if y == 0:
            return True
        # 보의 한쪽 끝 부분 위에 있거나
        if (x-1, y) in beams or (x, y) in beams: # 보의 오른쪽 끝 위 or 보의 왼쪽 끝 위
            return True
        # 다른 기둥 위에 있어야 함
        if (x, y-1) in pillars:
            return True
        return False
        
    def can_build_beam(x, y):
        # 한쪽 끝 부분이 기둥 위에 있거나 
        if (x, y-1) in pillars or (x+1, y-1) in pillars: # 보의 왼쪽 아래에 기둥 or 보의 오른쪽 아래에 기둥
            return True
        # 양쪽 끝 부분이 다른 보와 동시에 연결되어야 함
        if (x-1, y) in beams and (x+1, y) in beams:
            return True
        return False
        
    # 전체 구조물 상태 체크
    def is_everything_okay():
        for x, y in pillars:
            if not can_build_pillar(x, y):
                return False
        for x, y in beams:
            if not can_build_beam(x, y):
                return False
        return True
    
    for x, y, structure, action in build_frame:
        # 기둥
        if structure == 0:
            if action == 1 and can_build_pillar(x, y): # 설치
                pillars.add((x, y))
                if not is_everything_okay():
                    pillars.remove((x, y))
            elif action == 0 and (x, y) in pillars: # 삭제
                pillars.remove((x, y))
                if not is_everything_okay():
                    pillars.add((x, y))
        # 보
        else:
            if action == 1 and can_build_beam(x, y): # 설치
                beams.add((x, y))
                if not is_everything_okay():
                    beams.remove((x, y))    
            elif action == 0 and (x, y) in beams: # 삭제
                beams.remove((x, y))
                if not is_everything_okay():
                    beams.add((x, y))    
            
    for x, y in pillars:
        answer.append([x, y, 0])
    for x, y in beams:
        answer.append([x, y, 1])
        
    return sorted(answer)