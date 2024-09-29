import math

def solution(progresses, speeds):
    answer = []
    processing_time = []
    
    for (progress, speed) in zip(progresses, speeds):
            time = math.ceil((100 - progress) / speed)
            processing_time.append(time)
    
    # 첫 번째 작업을 기준으로 배포 그룹 만들기
    current_max_time = processing_time.pop(0) # 첫 번째 작업의 완료시간
    count = 1 # 첫 번째 작업은 항상 배포되므로 초기값 1
    
    while processing_time:
        time = processing_time.pop(0)
        
        # 만약 현재 작업이 앞선 작업과 함께 배포될 수 있는 경우
        if time <= current_max_time:
            count += 1
        else:
            # 새로운 배포 그룹을 형성하는 경우
            answer.append(count)
            current_max_time = time
            count = 1
        
    # 마지막 배포 그룹 처리
    answer.append(count)
    return answer