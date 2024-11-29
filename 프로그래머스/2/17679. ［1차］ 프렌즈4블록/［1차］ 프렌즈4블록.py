def solution(m, n, board):
    board = [list(row) for row in board]
    total_popped = 0
    
    while True:
        popped_count = pop(board)
        if popped_count == 0: # 더 이상 제거할 블록이 없으면 종료
            break
        total_popped += popped_count # 제거된 블록 개수 누적
        board = rearrange(board) # 빈 공간 채우기

    return total_popped

def pop(board):
    R = len(board)
    C = len(board[0])
    popped = set()
    
    for row in range(R - 1):
        for col in range(C - 1):
            cur = board[row][col]

            # 2 * 2 블록 탐색
            if (
                cur is not None and
                cur == board[row][col + 1] and 
                cur == board[row + 1][col] and 
                cur == board[row + 1][col + 1]
            ):
                popped.add((row, col)),
                popped.add((row, col + 1)),
                popped.add((row + 1, col)),
                popped.add((row + 1, col + 1))
    
    for row, col in popped:
        board[row][col] = None # 제거된 블록은 None으로 변경
    
    return len(popped)

def rearrange(board):
    R = len(board)
    C = len(board[0])
    
    for col in range(C):
        col_stack = []
        
        # 각 열에서 유효한 블록 추출
        for row in range(R):
            cur = board[row][col]
            if cur is not None:
                col_stack.append(cur)
        
        # 빈 칸 채우기
        empty_slots = [None] * (R - len(col_stack))
        col_stack = empty_slots + col_stack
            
        # 해당 열의 각 행을 순회하며 행의 값을 새로 채워넣음
        for row in range(R):
            board[row][col] = col_stack[row]
    
    return board
    
    