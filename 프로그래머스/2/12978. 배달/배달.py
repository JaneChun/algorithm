def solution(N, road, K):
    answer = 0

    graph = [{} for i in range(N + 1)]
    
    for v1, v2, time in road:
        if v1 in graph[v2]: # 중복 있을 경우 짧은 거리 사용
            time = min(graph[v1][v2], time)
        graph[v1][v2] = time
        graph[v2][v1] = time
        
    # BFS를 사용해 최소 시간 계산
    dist = [float('inf')] * (N + 1)
    dist[1] = 0
    
    queue = [(1, 0)] # 현재 마을, 누적 시간
    
    while queue:
        cur, cur_time = queue.pop(0)
        
        for neighbor, time in graph[cur].items():
            new_time = cur_time + time
            if new_time < dist[neighbor]:
                dist[neighbor] = new_time # 최단시간 갱신
                queue.append((neighbor, new_time))
                
    return sum(1 for time in dist if time <= K)

    return answer