def solution(n, k, enemy):
    answer = 0
    
    def is_possible(round):
        rounds = enemy[:round]
        left_enemys = sum(sorted(rounds, reverse=True)[k:])
        if n >= left_enemys:
            return True
        else:
            return False
        
    # 몇라운드가 최대인지 이진 탐색으로 찾는다.
    left = 1
    right = len(enemy)
    mid = (left + right) // 2 # 최대 라운드 추측값
    
    while left <= right:
        print(right)
        mid = (left + right) // 2
        # mid로 꺨 수 있는지 확인
        # 깼으면 더 깰 수 있는지 확인
        if is_possible(mid):
            answer = max(answer, mid)
            left = mid + 1
        # 못깼으면 라운드 줄이면 깰 수 있는지 확인
        else:
            right = mid - 1
    
    return answer