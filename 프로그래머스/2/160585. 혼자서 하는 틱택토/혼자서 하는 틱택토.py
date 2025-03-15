def solution(board):
    flatten = ''.join(board)
    o_count = flatten.count('O')
    x_count = flatten.count('X')
    
    o_win = is_winner(board, 'O')
    x_win = is_winner(board, 'X')
    
    if o_count < x_count or o_count > x_count + 1:
        return 0

    # 둘 다 이기는 건 불가능
    if o_win and x_win:
        return 0
    
    # O가 이긴 경우 X보다 1 많아야 함
    if o_win and o_count != x_count + 1:
        return 0
        
    # X가 이긴 경우 O와 개수가 같아야 함
    if x_win and o_count != x_count:
        return 0
    
    return 1

def is_winner(board, symbol):
    # 가로
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == symbol:
            return True
    
    # 세로 
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] == symbol:
            return True
        
    # 대각선
    if board[0][0] == board[1][1] == board[2][2] == symbol:
        return True
    elif board[0][2] == board[1][1] == board[2][0] == symbol:
        return True
    
    return False

# ["OOO", 
#  "XOX", 
#  "XXO"]