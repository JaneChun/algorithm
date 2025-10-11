# def solution(board, skill):
#     N = len(board)
#     M = len(board[0])
#     answer = 0
    
#     for s in skill:
#         t, r1, c1, r2, c2, degree = s
        
#         # 적의 공격
#         if t == 1:
#             for r in range(r1, r2 + 1):
#                 for c in range(c1, c2 + 1):
#                     board[r][c] -= degree
#         else: # 아군의 회복
#             for r in range(r1, r2 + 1):
#                 for c in range(c1, c2 + 1):
#                     board[r][c] += degree
    
#     for r in range(N):
#         for c in range(M):
#             if board[r][c] > 0:
#                 answer += 1
    
    # return answer
# 사각형 범위마다 직접 반복문을 돌리면 스킬의 길이가 K일 때
# => K * N * M 의 시간복잡도

def solution(board, skill):
    # 누적합을 이용한 풀이
    # 1. skill의 r1, c1, r2, c2에 대해서 r1: degree / r2 + 1: -degree / c1: degree / c2 + 1: -degree로 누적합 계산을 위한 숫자 표시
    # 2. 행 누적합 먼저 계산 후, 열 누적합 계산
    # 3. board를 한번 순회하며 각 셀에 누적합을 더해준다.
    
    # e.g. r1, c1, r2, c2 = [1, 0, 3, 1] degree = 2 일 때
    # 0 0  0 0 0 (0 --- 임의의 열
    # 2 0 -2 0 0  0 
    # 0 0  0 0 0  0  
    # 0 0  0 0 0  0
  # (-2 0  2 0 0  0) --- 임의의 행

    # 행 누적합 계산 후
    # 0 0  0 0 0 0 
    # 2 0 -2 0 0 0 
    # 2 0 -2 0 0 0  
    # 2 0 -2 0 0 0
    # 0 0  0 0 0 0
    
    # 열 누적합 계산 후
    # 0 0 0 0 0 0
    # 2 2 0 0 0 0 
    # 2 2 0 0 0 0  
    # 2 2 0 0 0 0
    # 0 0 0 0 0 0
    
    N = len(board)
    M = len(board[0])
    answer = 0
    
    acc = [[0 for _ in range(M + 1)] for _ in range(N + 1)]
    
    for s in skill:
        t, r1, c1, r2, c2, degree = s # [1, 0, 3, 1]
        
        if t == 1:
            degree = -degree
        
        acc[r1][c1] += degree
        acc[r1][c2 + 1] -= degree
        acc[r2 + 1][c1] -= degree
        acc[r2 + 1][c2 + 1] += degree
    
    # 행 누적합 계산
    for c in range(M):
        for r in range(1, N):
            acc[r][c] += acc[r - 1][c]
    
    # 열 누적합 계산
    for r in range(N):
        for c in range(1, M):
            acc[r][c] += acc[r][c - 1]
        
    # board에 누적합 더해주기
    for r in range(N):
        for c in range(M):
            board[r][c] += acc[r][c]
        
    # 파괴되지 않은 건물 계산
    for r in range(N):
        for c in range(M):
            if board[r][c] > 0:
                answer += 1
                
    return answer
    
    