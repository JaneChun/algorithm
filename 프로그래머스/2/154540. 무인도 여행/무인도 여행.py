def solution(maps):
    answer = []
    
    row_len = len(maps)
    col_len = len(maps[0])
    
    visited = [[False for _ in range(col_len)] for _ in range(row_len)] # 전역에서 관리
    
    def bfs(start_y, start_x):
        queue = [[start_y, start_x]]
        total_days = int(maps[start_y][start_x])
        
        direction = [[-1, 0], [0, -1], [1, 0], [0, 1]]
        
        while queue:
            y, x = queue.pop(0)
            visited[y][x] = True
            
            for dx, dy in direction:            
                nx = x + dx
                ny = y + dy

                if (
                    0 <= nx < col_len and 
                    0 <= ny < row_len and 
                    maps[ny][nx] != 'X' and
                    not visited[ny][nx]
                ):
                    queue.append([ny, nx])
                    total_days += int(maps[ny][nx])
                    visited[ny][nx] = True
        
        return total_days
    
    for y in range(row_len):
        for x in range(col_len):
            if maps[y][x] != 'X' and not visited[y][x]:
                result = bfs(y, x)
                answer.append(result)

    return sorted(answer) if len(answer) else [-1]