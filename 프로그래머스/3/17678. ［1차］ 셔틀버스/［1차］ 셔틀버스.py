# 셔틀 운행 횟수 n, 셔틀 운행 간격 t, 한 셔틀에 탈 수 있는 최대 크루 수 m
# 크루가 대기열에 도착하는 시각을 모은 배열 timetable

# 콘이 도착해야 하는 시간 = 마지막 셔틀에 타기 위해 도착해야 하는 가장 늦은 시간
# 셔틀에 자리가 있으면 → 출발 시각까지
# 셔틀에 자리가 없으면 → 마지막 탑승 크루보다 1분 일찍
def solution(n, t, m, timetable):
    answer = ''
    crew_time = []
    
    for time in timetable:
        hh, mm = time.split(':')
        crew_time.append(int(hh) * 60 + int(mm))
    
    crew_time.sort()
    # print(crew_time)
    # [480, 549, 550]
        
    # 셔틀 출발 시간
    schedule = []

    cur = 9 * 60 # 9:00
    for i in range(1, n + 1):
        schedule.append(cur)
        cur += t
    # print(schedule)
    # [540, 550]
    
    # crew_time 배열에서 bus_time보다 작거나 같은 사람들을 최대 m명만큼 태울 수 있음
    for index, bus_time in enumerate(schedule):
        capacity = int(m)
        while capacity > 0 and crew_time and crew_time[0] <= bus_time:
            onboarding_crew = crew_time.pop(0)
            capacity -= 1
            # print(index + 1, '번째 버스', onboarding_crew, '탑승')
            
            # 만약 현재 버스가 마지막 버스이고, capacity가 1이라면, onboarding_crew보다 1분 빨리 와서 타야함
            if index == len(schedule) - 1 and capacity == 0:
                last_time = onboarding_crew - 1
                return transform_to_time_string(last_time)
            
    return transform_to_time_string(schedule[-1])

def transform_to_time_string(mm):
    hour = mm // 60
    minutes = mm % 60
    
    return f"{hour:02d}:{minutes:02d}"  # 2자리 숫자로 맞춤, 09:00 형태