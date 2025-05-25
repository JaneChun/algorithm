from collections import defaultdict

def solution(edges):
    graph = defaultdict(list)
    in_count = defaultdict(int)
    out_count = defaultdict(int)
    
    for a ,b in edges:
        graph[a].append(b)
        out_count[a] += 1
        in_count[b] += 1
        
    # 생성한 정점(G) 찾기: 진입차수 0 이면서 진출차수 >= 2
    G = None
    for node in out_count:
        if in_count[node] == 0 and out_count[node] >= 2:
            G = node    
            break
    
    # G에 직접 연결된 정점들을 시작으로 각각의 그래프를 dfs로 탐색
    visited = set()
    
    def dfs(node):
        stack = [node]
        visited.add(node)
        v_count = 1
        e_count = 0
        
        while stack:
            cur = stack.pop()
            
            for neighbor in graph[cur]:
                e_count += 1
                
                if neighbor not in visited:
                    visited.add(neighbor)
                    v_count += 1
                    stack.append(neighbor)
                    
        return v_count, e_count
        
        
    donut, stick, eight = 0, 0, 0
        
    for start in graph[G]:
        if start in visited: 
            continue
            
        v, e = dfs(start)
        
        if v == e: # 정점 수 == 간선 수 → 도넛
            donut += 1
        elif v - 1 == e: # 정점 수 - 1 == 간선 수 → 막대
            stick += 1
        elif v + 1 == e: # 정점 수 + 1 == 간선 수 → 8자
            eight += 1

    return [G, donut, stick, eight]