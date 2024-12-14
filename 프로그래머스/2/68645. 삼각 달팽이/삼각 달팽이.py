def solution(n):
    max_num = (n * (n + 1)) // 2
    # 2차원 배열
    matrix = [[0] * n for _ in range(n)]
    direction = [[1, 0], [0, 1], [-1, -1]]
    dir_idx = 0
    cur_row, cur_col = 0, 0
    
    for i in range(1, max_num + 1):
        matrix[cur_row][cur_col] = i # 현재 위치에 숫자 채우기
        
        # 다음 위치 계산
        d_row, d_col = direction[dir_idx]
        next_row = cur_row + d_row
        next_col = cur_col + d_col
        
        # 다음 위치가 유효한 위치인지 확인 후, 아니라면 
        if not (0 <= next_row < n and 0 <= next_col < n and matrix[next_row][next_col] == 0):
            dir_idx = (dir_idx + 1) % 3 # 방향 전환
            d_row, d_col = direction[dir_idx]
            next_row = cur_row + d_row # 다음 위치 재할당
            next_col = cur_col + d_col
        
        # 다음 위치로 이동
        cur_row = next_row
        cur_col = next_col
        
    answer = []
    
    for row in range(n):
        for col in range(n):
            if matrix[row][col] != 0:
                answer.append(matrix[row][col])
    
    return answer

# [1, 0, 0, 0
#  2, 9, 0, 0
#  3, 10,8, 0
#  4, 5, 6, 7]

# 달팽이 모양 순서
# 1. x는 그대로 y만 증가 (n번)
# 2. x만 증가, y는 그대로 (n-1번)
# 3. x 감소, y도 감소 (n-2번)
# 4. 1번부터 반복