import heapq

def dijkstra(n, graph, s):
    distances = [float('inf')] * (n + 1) # S에서 i까지 가는 최단 경로(=최소 요금)
    q = [(0, s)] # 짧은 간선부터 탐색하도록 우선순위 큐(최소 힙) 사용 # (거리, 노드)
    
    while q:
        dist, node = heapq.heappop(q)
        
        # 이미 처리된 경우 스킵
        if dist > distances[node]:
            continue
        
        # 방문한 적 없거나 더 짧은 거리라면 갱신하고 -> 이어서 연결된 노드 탐색
        distances[node] = dist
        
        for i in range(1, n + 1):
            next_dist = graph[node][i]
            if next_dist != 0:
                heapq.heappush(q, (dist + next_dist, i)) # 거리 합산
    
    return distances

def solution(n, s, a, b, fares):
    graph = {i: [0] * (n + 1) for i in range(1, n + 1)}
    
    for c, d, f in fares:
        graph[c][d] = f
        graph[d][c] = f
        
    # 각 노드에서 그래프의 모든 다른 노드까지의 최단 거리를 구한다.
    dist_s = dijkstra(n, graph, s)
    dist_a = dijkstra(n, graph, a)
    dist_b = dijkstra(n, graph, b)
    
    # 구한 최단거리를 이용해서 s -> a -> b 또는 s -> b -> a 또는 s -> a + s -> b 중 최소값을 리턴한다.
    # op1 = dist_s[a] + dist_a[b]
    # op2 = dist_s[b] + dist_b[a]
    # op3 = dist_s[a] + dist_s[b]
    # return min(op1, op2, op3)
    # => 이 경우, 중간의 다른 노드를 거쳐서 가는(e.g. 5) 경우를 고려하지 못함
    
    answer = float('inf')
    for i in range(1, n + 1):
        total = dist_s[i] + dist_a[i] + dist_b[i]
        if total < answer:
            answer = total
    
    return answer