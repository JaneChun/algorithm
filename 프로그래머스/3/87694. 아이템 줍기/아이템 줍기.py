#  테두리를 따라 가는 올바른 경로: (3,6) ← (4,6)
#                                     ↑
#                           (3,5) → (4,5)

# 하지만 만약테두리를 1칸짜리 셀로 표현하면
# y
# 6   ■ ■
# 5   ■ ■
#     3 4 x

# BFS 입장에서는 (3,6)
#               ↑
#             (3,5) 으로 이동한다.

def solution(rectangle, characterX, characterY, itemX, itemY):
    board = [[0] * 102 for _ in range(102)]
    
    # 직사각형 영역 1로 채우기
    for x1, y1, x2, y2 in rectangle:
        x1 *= 2; y1 *= 2; x2 *= 2; y2 *= 2 # 좌표 2배
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                board[x][y] = 1
    
    # 테두리 제외한 내부 지우기
    for x1, y1, x2, y2 in rectangle:
        x1 *= 2; y1 *= 2; x2 *= 2; y2 *= 2 # 좌표 2배
        for x in range(x1 + 1, x2):
            for y in range(y1 + 1, y2):
                board[x][y] = 0
            
    # BFS로 테두리(board[x][y] == 1)만 이동하기
    d = [(1, 0), (-1, 0), (0, -1), (0, 1)]
    q = [(characterX*2, characterY*2, 0)] # 좌표 2배
    visited = set()
    
    while q:
        cur_x, cur_y, cur_dis = q.pop(0)
        
        # 아이템 도착
        if cur_x == itemX*2 and cur_y == itemY*2: # 좌표 2배
                return cur_dis // 2 # 거리 원래대로
        
        # 상하좌우 탐색
        for dx, dy in d:
            next_x, next_y, next_dis = cur_x + dx, cur_y + dy, cur_dis + 1
            
            if board[next_x][next_y] == 1 and (next_x, next_y) not in visited:
                q.append((next_x, next_y, next_dis))
                visited.add((next_x, next_y))
        
    return -1