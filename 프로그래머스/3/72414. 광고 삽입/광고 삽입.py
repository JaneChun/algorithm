def hhmmss_to_seconds(hhmmss):
    h, m, s = map(int, hhmmss.split(':'))
    return h * 3600 + m * 60 + s

def seconds_to_hhmmss(seconds):
    h = seconds // 3600
    m = (seconds % 3600) // 60
    s = seconds % 60
    return f"{h:02}:{m:02}:{s:02}"

def solution(play_time, adv_time, logs):
    answer = ''
    
    total_seconds = hhmmss_to_seconds(play_time)
    adv_seconds = hhmmss_to_seconds(adv_time)
    
    # 각 초의 시청자 변화량
    viewer_changes = [0] * (total_seconds + 1) 
    
    for log in logs:
        start_str, end_str = log.split('-')
        start = hhmmss_to_seconds(start_str)
        end = hhmmss_to_seconds(end_str)
        
        viewer_changes[start] += 1
        viewer_changes[end] -= 1
    
    # 각 초별 시청자 변화량을 배열에 누적합을 사용해 -> 각 초의 시청자수 구하기
    viewer_count = [0] * (total_seconds + 1) # viewer_count[i] = i초에 보고있는 시청자수
    viewer_count[0] = viewer_changes[0]
    
    for i in range(1, len(viewer_changes)):
        viewer_count[i] = viewer_count[i-1] + viewer_changes[i]
        
    # 각 초별 시청자수 배열에 누적합을 사용해 -> 각 초까지의 누적 시청시간 구하기
    view_acc = [0] * (total_seconds + 1) # view_acc[i] 0초부터 i초까지의 누적 시청시간
    view_acc[0] = viewer_count[0]
    
    for i in range(1, len(viewer_count)):
        view_acc[i] = view_acc[i-1] + viewer_count[i]
    
    # 총 재생시간(total_seconds)에서 광고 길이(adv_seconds)를 넣을 수 있는 모든 구간 탐색
    max_watch = view_acc[adv_seconds - 1] # 초기값: 0 ~ adv_seconds까지의 누적 시청 시간
    best_start = 0

    for start in range(1, total_seconds - adv_seconds + 1):
        end = start + adv_seconds - 1

        current_watch = view_acc[end] - view_acc[start - 1]

        if current_watch > max_watch:
            max_watch = current_watch
            best_start = start

    return seconds_to_hhmmss(best_start)