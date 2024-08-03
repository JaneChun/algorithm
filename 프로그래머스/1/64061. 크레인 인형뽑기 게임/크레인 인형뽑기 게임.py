def solution(board, moves):
    newBoard = []
    for i in range(len(board)):
        newBoard.append([]) # [[], [], [], [], []]
    
    for row in range(len(board) - 1, -1, -1): # 맨 아랫줄부터 4, 3, 2, 1, 0
        for col in range(len(board)): # 0 1 2 3 4
            item = board[row][col]
            if item != 0:
                newBoard[col].append(item)
    
    count = 0
    stack = []
    for move in moves:
        if newBoard[move - 1]:
            stack.append(newBoard[move - 1].pop())
    
    count = 0
    result = []
    for item in stack:
        if result and result[-1] == item:
            result.pop()
            count += 2
        else:
            result.append(item)
    
    return count