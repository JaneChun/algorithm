# 사이클: 같은 시작 지점 + 같은 방향으로 다시 돌아올 때
def solution(grid):
    answer = []
    
    rows = len(grid)
    cols = len(grid[0])
    visited = set() # x, y, d
    
    # 상, 우, 하, 좌
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    
    for x in range(rows):
        for y in range(cols):
            for d in range(4):
                # visted에 있는 경우, 이전에 탐색한 사이클과 경로가 똑같으므로 제외
                if (x, y, d) in visited:
                    continue
                    
                # 사이클 시작점    
                count = 0
                cx, cy, cd = x, y, d
                
                # 사이클이 종료될 때까지(같은 칸, 같은 방향을 만날 때까지) 이동을 반복
                while not (cx, cy, cd) in visited:
                    visited.add((cx, cy, cd))
                    count += 1
                    
                    # 방향 전환
                    cd = turn(cd, grid[cx][cy])
                    
                    # 이동
                    cx = (cx + dx[cd]) % rows
                    cy = (cy + dy[cd]) % cols
                
                answer.append(count)

    return sorted(answer)

def turn(direction, cell):
    if cell == 'L':
        return (direction - 1) % 4
    elif cell == 'R':
        return (direction + 1) % 4
    return direction