def solution(h1, m1, s1, h2, m2, s2):
    answer = 0
    
    # 초 단위로 변환
    start = h1 * 60 * 60 + m1 * 60 + s1
    end = h2 * 60 * 60 + m2 * 60 + s2
    
   # 시작 시간이 00:00:00 또는 12:00:00이여서 초침, 분침, 시침이 정확히 겹치는 경우
    if start % (12 * 3600) == 0:
        answer += 1
        
    while start < end:
        #  초침, 분침, 시침의 현재 각도
        h = (start / 120) % 360 # 1시간에 360도 -> 360 / 60 * 60 * 12 = 1초에 1/120도
        m = (start / 10) % 360 # 60분에 360도 -> 360 / 60 * 60 = 1초에 1/10도
        s = (start * 6) % 360 # 60초에 360도 -> 360 / 60 = 1초에 6도
        
        # 다음 초의 각도 계산 (아래 비교를 위해 0을 360으로 간주)
        n_h = 360 if (start + 1) / 120 % 360 == 0 else (start + 1) / 120 % 360
        n_m = 360 if (start + 1) / 10 % 360 == 0 else (start + 1) / 10 % 360
        n_s = 360 if (start + 1) * 6 % 360 == 0 else (start + 1) * 6 % 360
        
        # 초침이 시침을 지나친 경우
        if s < h and n_s >= n_h:
            answer += 1
        # 초침이 분침을 지나친 경우
        if s < m and n_s >= n_m:
            answer += 1
        # 초침, 분침, 시침이 모두 겹치는 경우: 알람이 2번 울렸으므로 한번 제거
        if n_s == n_m and n_s == n_h:
            answer -= 1
        
        start += 1
    
    return answer