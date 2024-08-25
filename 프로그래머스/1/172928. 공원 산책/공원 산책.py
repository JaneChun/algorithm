def solution(park, routes):
    H = len(park)
    W = len(park[0])
    x, y = 0, 0
    
    # 'S'의 위치 찾기
    for i, row in enumerate(park):
        for j, char in enumerate(row):
            if char == 'S':
                x = j
                y = i
                break
    
    directions = {
        'E': {'x': 1, 'y': 0},
        'W': {'x': -1, 'y': 0},
        'S': {'x': 0, 'y': 1},
        'N': {'x': 0, 'y': -1},
    }
    
    for route in routes:
        direction, num = route.split(' ')
        next_x = x
        next_y = y
        valid_move = True  # 이동이 유효한지 여부를 추적하는 변수
        
        for i in range(int(num)):
            # 이동
            next_x = next_x + directions[direction]['x']
            next_y = next_y + directions[direction]['y']
            
            # 범위를 벗어나지 않는지 체크
            if not (0 <= next_x < W and 0 <= next_y < H):
                valid_move = False
                break

            # 장애물 체크
            if park[next_y][next_x] == 'X':
                valid_move = False
                break
        
        if valid_move:
            x, y = next_x, next_y
            
    return [y, x]