def solution(players, m, k):
    answer = 0
    servers = [-1] # 기본 서버 1대. 종료시간은 무한
    
    for i, player in enumerate(players):
        # 매 시간 만료된 서버를 종료
        servers = list(filter(lambda x: x != i, servers))
        
        capacity = len(servers) * m
        
        if capacity <= player:
            # 부족한 만큼 서버 증설
            extra_need_server_cnt = ((player - capacity) // m) + 1
            for _ in range(extra_need_server_cnt):
                servers.append(i + k) # 종료 시간 입력 
                answer += 1
            
    return answer