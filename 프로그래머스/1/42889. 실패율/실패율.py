def solution(N, stages):
    answer = []
    cur_users = len(stages)
    
    for i in range(1, N + 1):
        fail_users = 0
        
        for user in stages:
            if user == i:
                fail_users += 1
                    
        fail_ratio = 0 if fail_users == 0 else fail_users / cur_users
        answer.append([i, fail_ratio])
        cur_users -= fail_users
    
    sorted_answer = sorted(answer, key=lambda x: (-x[1]))
    
    return [x[0] for x in sorted_answer]