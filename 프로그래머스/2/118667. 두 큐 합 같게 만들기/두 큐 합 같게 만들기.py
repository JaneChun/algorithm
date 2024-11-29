def solution(queue1, queue2):
    total_sum = sum(queue1) + sum(queue2)
    if total_sum % 2 == 1: # 두 수의 합이 홀수라면 답은 무조건 -1
        return -1

    each_sum = total_sum // 2 # 각 큐가 가져야 할 목표 합
    combined_queue = queue1 + queue2 # 두 큐를 연결
    
    left = 0
    right = len(queue1) 
    queue1_sum = sum(queue1)
    
    for i in range(len(combined_queue) * 2): # 최대 이동 횟수 제한
        if queue1_sum == each_sum: # 목표 합에 도달한 경우
            return i
        elif queue1_sum < each_sum: #  합이 부족하면 right 포인터 이동
            queue1_sum += combined_queue[right]
            right += 1
        else: # 합이 초과하면 left 포인터 이동
            queue1_sum -= combined_queue[left]
            left += 1
            
        # right 포인터가 전체 길이를 초과할 경우 루프 종료
        if right > len(combined_queue) - 1:
            return -1