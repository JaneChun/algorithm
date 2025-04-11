from copy import deepcopy

def solution(storage, requests):
    n, m = len(storage), len(storage[0])
    storage = list(map(lambda x: list(x), storage))
    
    for request in requests:
        if len(request) ==  1:
            storage = use_forklift(n, m, storage, request)
        else:
            storage = use_crain(n, m, storage, request[0])
    
    return sum(x is not None for row in storage for x in row)

def use_crain(n, m, storage, container):
    for i in range(n):
        for j in range(m):
            if storage[i][j] == container:
                storage[i][j] = None
                
    return storage

def use_forklift(n, m, storage, container):
    snapshot = deepcopy(storage)
    
    for i in range(n):
        for j in range(m):
            # 가장자리거나, 나갈 길이 있는 경우
            if storage[i][j] == container and (is_edge(n, m, i, j) or is_accessible(n, m, snapshot, i, j)):
                storage[i][j] = None
            
    return storage

def is_edge(n, m, y, x):
    return y == 0 or y == n - 1 or x == 0 or x == m - 1

# bfs로 상하좌우 탐색해 밖으로 통하는 길이 있는지 확인
def is_accessible(n, m, snapshot, i, j):
    queue = []
    visited = [[False] * m for _ in range(n)]

    queue.append([i, j])
    visited[i][j] = True

    while queue:
        y, x = queue.pop(0)
        # 현재 칸이 가장자리인 경우
        if is_edge(n, m, y, x):
            return True

        for dx, dy in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
            nx, ny = x + dx, y + dy

            # 외부가 아니지만 None이여서 지나갈 수 있는 경우
            if (0 <= nx < m and 
                0 <= ny < n and 
                not visited[ny][nx] and 
                snapshot[ny][nx] is None):
                queue.append([ny, nx])
                visited[ny][nx] = True

    return False