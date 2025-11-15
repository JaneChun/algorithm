from collections import deque

def solution(info, edges):
    answer = 1
    
    # 그래프 생성
    graph = {i: [] for i in range(len(info))}
    
    for parent, child in edges:
        graph[parent].append(child)
    
    # bfs로 탐색
    # queue = [{노드, 양, 늑대, [인접노드들]}]
    # 현재 탐색중인 노드에서 양의 수 > 늑대 수 라면 queue에 인접노드들을 추가
    
    q = deque()
    q.append((0, 1, 0, graph[0]))
    visited = set()
    
    while q:
        cur, sheep, wolf, neighbors = q.popleft()
        
        # 이미 탐색한 경로라면 스킵
        neighbors_str = str(sorted(neighbors))
        if neighbors_str in visited:
            continue
            
        for nxt in neighbors:
            nxt_sheep = sheep
            nxt_wolf = wolf
            if info[nxt] == 0:
                nxt_sheep += 1
            else:
                nxt_wolf += 1
            
            if nxt_sheep > nxt_wolf:
                nxt_neighbors = list(set(graph[nxt] + neighbors) - {cur, nxt}) # 뒤로 돌아갈 수 있음
                q.append((nxt, nxt_sheep, nxt_wolf, nxt_neighbors))
                visited.add(neighbors_str)
                answer = max(answer, nxt_sheep)
    
    return answer