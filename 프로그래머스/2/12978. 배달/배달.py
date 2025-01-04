def solution(N, road, K):
    answer = 0

    graph = [{} for i in range(N + 1)]
    
    for v1, v2, time in road:
        if v1 in graph[v2]: # 중복 있을 경우 짧은 거리 사용
            time = min(graph[v1][v2], time)
        graph[v1][v2] = time
        graph[v2][v1] = time
    print(graph)
        
    # BFS를 사용해 최소 시간 계산
    dist = [float('inf')] * (N + 1)
    dist[1] = 0 # [inf, 0, inf, inf ...]
    
    queue = [(1, 0)] # 현재 마을, 누적 시간
    
    while queue:
        cur, cur_time = queue.pop(0)
        
        for neighbor, time in graph[cur].items(): # {2: 1, 4: 2}
            new_time = cur_time + time # 1
            if new_time < dist[neighbor]: # 1 < inf
                dist[neighbor] = new_time # 최단시간 갱신
                queue.append((neighbor, new_time))
    print(dist)
                
    return sum(1 for time in dist if time <= K)

    return answer