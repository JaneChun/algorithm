from datetime import datetime, timedelta

def solution(plans):
    answer = []
    left_stack = []
    
    # datetime 객체로 변환
    plans = list(map(lambda x: [x[0], datetime.strptime(x[1], "%H:%M"), int(x[2])], plans))
    plans.sort(key=lambda x: x[1])
    # print(plans)
    
    for i in range(len(plans) - 1):
        cur = plans[i]
        nxt = plans[i + 1]
        cur_name, cur_start, cur_playtime = cur
        nxt_name, nxt_start, nxt_playtime = nxt
        
        cur_end = cur_start + timedelta(minutes=cur_playtime)
        
        if cur_end <= nxt_start:
            answer.append(cur_name)
            
            # 남는 시간 동안 left_stack 진행
            extra_time = (nxt_start - cur_end).total_seconds() / 60
            while left_stack and extra_time:
                left = left_stack[-1]
                left_name, left_start, left_playtime = left
                
                if left_playtime <= extra_time:
                    left_stack.pop()
                    answer.append(left_name)
                    extra_time -= left_playtime    
                else:
                    left_stack[-1][2] = left_playtime - extra_time
                    extra_time = 0
                
        else:
            left_time = cur_playtime - (nxt_start - cur_start).total_seconds() / 60
            left_stack.append([cur_name, cur_start, left_time])
        
    # 마지막 plan 처리
    answer.append(plans[-1][0])

    # left_stack 남은 과제 처리
    while left_stack:
        left = left_stack.pop()
        answer.append(left[0])
    
    return answer