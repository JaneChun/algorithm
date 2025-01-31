def solution(board):
    answer = []
    ROW = len(board)
    COL = len(board[0])
    
    start = None
    
    # 시작 지점 찾기
    for row in range(ROW):
        for col in range(COL):
            if board[row][col] == 'R':
                start = [row, col]
                break
    
    direction = [[-1, 0], [1, 0], [0, 1], [0, -1]]
    queue = []
    visited = [[False for col in range(COL) ] for row in range(ROW)]
    
    # 시작 지점 queue에 넣고 상하좌우 탐색 시작
    queue.append([start, 0])
    visited[start[0]][start[1]] = True
    
    while queue:
        [[y, x], count] = queue.pop(0)
        
        if board[y][x] == 'G':
            answer.append(count)
        
        for dy, dx in direction:
            ny, nx = y, x
            # 해당 방향으로 보드의 끝 또는 D를 만날 때까지 슬라이딩
            while 0 <= ny + dy < ROW and 0 <= nx + dx < COL and board[ny + dy][nx + dx] != 'D':
                ny += dy
                nx += dx
            
            if not visited[ny][nx]:
                queue.append([[ny, nx], count + 1])
                visited[ny][nx] = True

    return min(answer) if len(answer) else -1