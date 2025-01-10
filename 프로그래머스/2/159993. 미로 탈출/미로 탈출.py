def solution(maps):
    COL_LENGTH = len(maps)
    ROW_LENGTH = len(maps[0])
    
    # 시작점, 종료점, 레버 찾기
    start, end, lever = None, None, None
    
    for y in range(COL_LENGTH):
        for x in range(ROW_LENGTH):
            if maps[y][x] == 'S':
                start = [y, x]
            if maps[y][x] == 'E':
                end = [y, x]
            if maps[y][x] == 'L':
                lever = [y, x]
    
    # BFS
    start_to_lever = BFS(maps, start, 'L')
    lever_to_end = BFS(maps, lever, 'E')
    
    if start_to_lever == -1 or lever_to_end == -1:
        return -1
                
    return start_to_lever + lever_to_end


def BFS(maps, start, target):
    COL_LENGTH = len(maps)
    ROW_LENGTH = len(maps[0])
    
    move = [[-1, 0], [1, 0], [0, -1], [0, 1]] # 상하좌우
    queue = [] 
    # visited = [[False] * COL_LENGTH] * ROW_LENGTH
    visited = [[False for _ in range(ROW_LENGTH)] for _ in range(COL_LENGTH)]
    
    # 시작점 세팅
    queue.append([start[0], start[1], 0]) # [y, x, time]
    visited[start[0]][start[1]] = True
    
    while queue:
        y, x, time = queue.pop(0)
        
        # 목표지점인 경우 시간 반환
        if maps[y][x] == target:
            return time
        
        # 상하좌우 탐색
        for dx, dy in move:
            next_x, next_y = x + dx, y + dy

            if (0 <= next_x < ROW_LENGTH and 
                0 <= next_y < COL_LENGTH and 
                maps[next_y][next_x] != 'X' 
                and not visited[next_y][next_x]
               ):
                visited[next_y][next_x] = True
                queue.append([next_y, next_x, time + 1])

    return -1


