def solution(m, n, puddles):
    MOD = 10 ** 9 + 7
    answer = 0

    # 0-based-index로 변환
    puddles = [[x - 1, y - 1] for x, y in puddles]
    
    dp = [[0] * m for _ in range(n)]
    dp[0][0] = 1
    
        
    for y in range(n):
        for x in range(m):
            # 최단거리로 y, x에 가는 방법의 가지수
            if [x, y] in puddles: # 웅덩이인 경우 갈 수 없음
                dp[y][x] = 0
                continue
            
            dp[y][x] += dp[y - 1][x]  + dp[y][x - 1]
            
    return dp[n - 1][m - 1] % MOD