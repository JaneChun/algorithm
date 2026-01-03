from collections import defaultdict
import heapq

def solution(n, paths, gates, summits):
    graph = defaultdict(list)
    
    for a, b, cost in paths:
        graph[a].append((b, cost))
        graph[b].append((a, cost))
        
    # 출발지에서부터 모든 정점까지의 최대 비용(intensity)를 저장
    # 나중에 산봉우리만 필터링하고 최소값을 구하면 됨
    
    ints = [float('inf')] * (n + 1) # 어떤 출발지에서 가든 각 정점까지 가는 경로 중 가장 큰 간선 비용의 최소값
    pq = []
    
    for gate in gates:
        ints[gate] = 0 # 출발지는 아직 간선을 타지 않았으므로 intensity = 0
        heapq.heappush(pq, (0, gate)) # 탐색 후보로 등록
        
    # 최소힙: 현재까지 가장 낮은 intensity를 가진 노드 선택
    while pq:
        cur_int, cur = heapq.heappop(pq) # 현재 intensity, 현재 노드
        
        if cur_int > ints[cur]: # 이미 더 적은 intensity로 간 기록이 있다면 스킵
            continue 
            
        if cur in summits: # 산봉우리에 도착하면 더 이상 확장하지 X
            continue
        
        for nxt, cost in graph[cur]: # 인접 노드 탐색
            # 다음 노드까지의 intensity 계산
            # 지금까지의 경로에서 가장 큰 간선 비용(cur_int)과
            # 새로 이동할 간선 비용(cost) 중 최대값
            nxt_int = max(cur_int, cost)
            
            # 더 작은 intensity로 갈 수 있는 경우에만 갱신
            if nxt_int < ints[nxt]:
                ints[nxt] = nxt_int
                heapq.heappush(pq, (nxt_int, nxt))
    
    summits.sort()
    answer = [0, float('inf')]

    for summit in summits:
        if ints[summit] < answer[1]:
            answer = [summit, ints[summit]]
            
    return answer