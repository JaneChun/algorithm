from collections import deque

def solution(board):
    N = len(board)
    directions = {
        'u': (-1, 0),
        'd': (1, 0),
        'r': (0, 1),
        'l': (0, -1)
    }
    
    cost = [[{d: None for d in directions} for _ in range(N)] for _ in range(N)]
    
    queue = deque()
    
    queue.append((0, 0, 'r', 0)) # 시작 오른쪽 방향
    queue.append((0, 0, 'd', 0)) # 시작 아래 방향
    cost[0][0]['r'] = 0
    cost[0][0]['d'] = 0
    
    while queue:
        y, x, d, c = queue.popleft()
        
        for nd, (dy, dx) in directions.items():
            ny = y + dy
            nx = x + dx
            nc = c + (100 if nd == d else 600) # 같은방향(직선도로)면 100, 아니면 500
            
            if (0 <= nx < N and 
                0 <= ny < N and 
                board[ny][nx] == 0 and # 길이 뚫려있고
                (cost[ny][nx][nd] is None or nc < cost[ny][nx][nd])): # 값을 입력한 적 없거나 기존 값보다 작은 경우에만 갱신                                
                queue.append((ny, nx, nd, nc))
                cost[ny][nx][nd] = nc
    
    last_values = cost[N-1][N-1].values()
    filtered_last_values = list(filter(lambda x: x is not None, last_values))
    return min(filtered_last_values)