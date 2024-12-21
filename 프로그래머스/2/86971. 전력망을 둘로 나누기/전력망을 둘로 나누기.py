def solution(n, wires):
    answer = float('inf')  # 최소값을 구해야 하므로 초기값을 큰 값으로 설정
    
    # 인접 리스트 생성
    graph = {i: [] for i in range(1, n + 1)}
    for v1, v2 in wires:
        graph[v1].append(v2)
        graph[v2].append(v1)
        
    # wires를 순회하며 간선을 하나씩 삭제
    for wire in wires:
        # 현재 간선 제거 (graph에서 간선을 제거)
        v1, v2 = wire
        graph[v1].remove(v2)
        graph[v2].remove(v1)
            
        # BFS로 하나의 네트워크의 크기 계산
        network1_size = bfs(v1, graph)
        network2_size = n - network1_size
        
        diff = abs(network1_size - network2_size) # 두 네트워크 크기 차이의 절대값
        answer = min(answer, diff) # 최소값 갱신
        
        # 제거한 간선 복구 (graph에 다시 추가)
        graph[v1].append(v2)
        graph[v2].append(v1)
        
    return answer 

def bfs(start, graph):
    queue = []
    visited = [False] * (len(graph) + 1) # 노드 방문 여부
    count = 0
    
    queue.append(start) # 탐색 시작 노드 추가
    visited[start] = True # 시작 노드 방문 처리
    
    while queue:
        cur = queue.pop(0) # 큐에서 현재 노드 꺼내고
        count += 1 # 방문한 노드 개수 증가
        
        # 현재 노드와 연결된 노드들 큐에 추가
        for neighbor in graph[cur]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
        
    return count