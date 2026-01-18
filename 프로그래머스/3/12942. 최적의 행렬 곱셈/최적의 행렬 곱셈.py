def solution(matrix_sizes):
    n = len(matrix_sizes)
    # dp[i][j] = i번째 행렬부터 j번째 행렬까지 곱하는 데 필요한 최소 연산횟수
    dp = [[float('inf') for j in range(n)] for i in range(n)]
    
    for i in range(n):
        for j in range(n):
            if i == j:
                dp[i][j] = 0 # 행렬 1개는 곱셈이 없으므로 연산횟수 = 0
                
    # 부분 행렬의 길이를 늘려가며 계산
    for size in range(2, n + 1):
        for i in range(0, n - size + 1):
            j = i + size - 1
            
            # 분할 기준 k: i ~ j를 (1 ~ k) x (k + 1 ~ j)로 분할하는 모든 경우를 탐색
            for k in range(i, j):
                # 비용 계산
                cost = (dp[i][k] 
                + dp[k+1][j] # k+1번부터 j번 행렬까지 곱하는데 필요한 최소 연산 횟수
                + (matrix_sizes[i][0] * matrix_sizes[k][1] * matrix_sizes[j][1]))
                # 두 부분 행렬을 곱할 때 필요한 연산 수 (A_i ... A_k) x (A_k+1 ... A_j) = (왼쪽 행 수 x 공통 차원 x 오른쪽 열 수)
                
                # 최소값 갱신
                dp[i][j] = min(dp[i][j], cost)
    
    # 0번 행렬부터 n-1번 행렬까지 다 곱한 결과(최소값)
    return  dp[0][n-1]