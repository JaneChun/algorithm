def solution(n, computers):
    answer = 0
    
    graph = []
    
    for i, connections in enumerate(computers):
        neighbors = []
        for j, connected in enumerate(connections):
            if i != j and connected == 1:
                 neighbors.append(j)
        graph.append(neighbors)
        
    
    visited = [False] * n
    
    def bfs(start): # 시작 지점부터 연결된 네트워크 모두 탐색하여 방문 처리
        queue = [start]
        visited[start] = True
        
        while queue:
            cur = queue.pop(0) 
            for neighbor in graph[cur]:
                if not visited[neighbor]:
                    queue.append(neighbor)
                    visited[neighbor] = True
            
        
    # graph: [[1], [0], []]
    for i in range(len(graph)):
        if not visited[i]: # 새로운 네트워크 발견
            bfs(i)
            answer += 1
    
    return answer