def solution(board):
    # 첫 번째 열, 첫 번째 행은 그대로 복사
    # 오른쪽 아래 = min(왼쪽 위, 위, 왼쪽)
    # 점화식: dp[i][j] = min(board[i - 1][j - 1], board[i - 1][j], board[i][j])
    
    row = len(board)
    col = len(board[0])
    max_size = 0
    
    dp = [[0] * col for _ in range(row)]
    
    for i in range(row):
        dp[i][0] = board[i][0]
        max_size = max(max_size, dp[i][0])
        
    for j in range(col):
        dp[0][j] = board[0][j]
        max_size = max(max_size, dp[0][j])
                
    for i in range(1, len(dp)): # 첫 줄 제외
        for j in range(1, len(dp[0])):
            if board[i][j] == 1:
                dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
                max_size = max(max_size, dp[i][j])

    return max_size ** 2