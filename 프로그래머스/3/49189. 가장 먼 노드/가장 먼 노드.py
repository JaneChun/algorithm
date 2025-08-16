from collections import defaultdict, deque

def solution(n, edge):
    answer = 0
    
    graph = defaultdict(list)
    
    for s, e in edge:
        graph[s].append(e)        
        graph[e].append(s)        
    
    # print(graph)
    # {3: [6, 4, 2, 1], 6: [3], 4: [3, 2], 2: [3, 1, 4, 5], 1: [3, 2], 5: [2]}
    
    dis_from_one = [0] * (n + 1)
    
    queue = deque([1])
    visited = [False] * (n + 1)
    visited[1] = True
    
    while queue:
        cur = queue.popleft() # [3, 2]

        for nxt in graph[cur]: # 3
            if not visited[nxt]:
                visited[nxt] = True
                dis_from_one[nxt] = dis_from_one[cur] + 1
                queue.append(nxt)
    
    return dis_from_one.count(max(dis_from_one))