# 재귀
# 꼭대기에서 경로의 최대 합 = 꼭대기에 있는 숫자 + MAX(왼쪽 대각선 삼각형에서 경로의 최대 합, 오른쪽 대각선 삼각형에서 경로의 최대 합)

# def solution(triangle):
#     def dfs(row, col):
#         if row == len(triangle) - 1: # 꼭대기 도착
#             return triangle[row][col] # 누적된 합 반환
        
#         return triangle[row][col] + max(dfs(row + 1, col), dfs(row + 1, col + 1))
    
#     return dfs(0, 0)

# 시간복잡도: O(2^H). 경로의 수가 이진트리처럼 매 단계마다 2배씩 증가하므로

# 동적계획법
def solution(triangle):
    dp = [[0] * (i + 1) for i in range(len(triangle))]
    # [[0], [0, 0], [0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0, 0]]
    
    for r in range(len(triangle) - 1, -1, -1):
        for c in range(len(triangle[r])):
            if r == len(triangle) - 1: # 맨 아래 행인 경우
                dp[r][c] = triangle[r][c]
                continue
                
            dp[r][c] = triangle[r][c] + max(dp[r + 1][c], dp[r + 1][c + 1]) # 꼭대기 + max(왼쪽 아래, 오른쪽 아래)
            
    
    return dp[0][0]
    
    
    