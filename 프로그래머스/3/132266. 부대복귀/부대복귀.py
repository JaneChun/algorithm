# from collections import defaultdict, deque

# def solution(n, roads, sources, destination):
#     answer = []
    
#     graph = defaultdict(list)
    
#     for a, b in roads:
#         graph[a].append(b)
#         graph[b].append(a)
    
#     for src in sources:
#         answer.append(get_distance(src, destination, graph, n))
    
#     return answer

# def get_distance(src, dest, graph, n):
#     queue = deque([(src, 0)])
#     visited = [False] * (n + 1)
    
#     while queue:
#         cur, dist = queue.popleft()
#         if cur == dest:
#             return dist
        
#         for neighbor in graph[cur]:
#             if not visited[neighbor]:
#                 visited[neighbor] = True
#                 queue.append((neighbor, dist + 1))
        
#     return -1
# 시간초과 -> sources마다 BFS 반복 X, 한 번의 BFS로 모든 sources까지의 거리를 구할 수 있음

from collections import defaultdict, deque

def solution(n, roads, sources, destination):
    # 인접 리스트 생성
    graph = defaultdict(list)
    
    for a, b in roads:
        graph[a].append(b)
        graph[b].append(a)
    
    # 거리 계산
    distances = [-1] * (n + 1)
    distances[destination] = 0
    queue = deque([destination])
    
    while queue:
        cur = queue.popleft()
        
        for nxt in graph[cur]:
            if distances[nxt] == -1:
                distances[nxt] = distances[cur] + 1 
                queue.append(nxt)
    
    return [distances[src] for src in sources]