def solution(points, routes):
    answer = 0
    
    time_dict = {} # {(시간, 행, 열): 0}

    for route in routes:
        time = 0
        
        # 시작 위치 기록
        src_num = route[0]
        src_r, src_c = points[src_num - 1]
        time_dict[(time, src_r, src_c)] = time_dict.get((time, src_r, src_c), 0) + 1
        
        for i in range(len(route) - 1):
            src_num = route[i]
            dest_num = route[i + 1]

            src_r, src_c = points[src_num - 1] # index로 변환
            dest_r, dest_c = points[dest_num - 1]

            # row 부터 이동
            while src_r != dest_r:
                src_r += 1 if src_r < dest_r else -1
                time += 1 # 이동과 시간 흐름

                time_dict[(time, src_r, src_c)] = time_dict.get((time, src_r, src_c), 0) + 1 # 현재 위치 기록

            # col 이동
            while src_c != dest_c:
                src_c += 1 if src_c < dest_c else -1
                time += 1

                time_dict[(time, src_r, src_c)] = time_dict.get((time, src_r, src_c), 0) + 1

    for value in time_dict.values():
        if value > 1:
            answer += 1
    
    return answer