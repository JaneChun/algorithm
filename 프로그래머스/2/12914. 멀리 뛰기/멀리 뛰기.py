# def solution(n):
#     answer = 0
    
#     def dfs(sum_value):
#         nonlocal answer # 외부의 answer 변수를 사용
#         if sum_value == n:
#             answer += 1
#             return
#         elif sum_value > n:
#             return
#         else:
#             dfs(sum_value + 1)
#             dfs(sum_value + 2)
    
#     dfs(0)
    
#     return answer

# DFS를 이용한 방법은 모든 가능한 경로를 탐색하기 때문에 시간복잡도가 높다.
# 현재의 DFS 방식의 시간 복잡도는 𝑂(2𝑛). 왜냐하면 각 단계에서 두 가지 선택(1 또는 2를 더하는)을 하기 때문에 모든 가능한 경로를 탐색하게 되기 때문

# 시간 복잡도를 줄이는 방법은 동적 계획법을 사용하는 것
# 메모이제이션(Memoization)을 사용하면 작은 문제의 결과를 저장하고 이를 재사용할 수 있기 때문에, 중복 계산을 피할 수 있습니다.

# 1까지 가는법 : 1개
    # 1

# 2까지 가는법 : 2개
    # 1 + 1
    # 2
    
# 3까지 가는 법 : 3개
    # 1 + 2

    # 1 + 1 + 1
    # 2 + 1

# 4까지 가는 법 : 5개
    # 1 + 1 + 2
    # 2 + 2

    # 1 + 1 + 1 + 1
    # 2 + 1 + 1
    # 1 + 2 + 1

# 5까지 가는 법 :
    # 1 + 2 + 2 (3에 2 더하기)
    # 1 + 1 + 1 + 2
    # 2 + 1 + 2

    # 1 + 1 + 2 + 1 (4에 1 더하기)
    # 2 + 2 + 1
    # 1 + 1 + 1 + 1 + 1
    # 2 + 1 + 1 + 1
    # 1 + 2 + 1 + 1

def solution(n):
    dp = [0, 1, 2]
    
    if n <= 2:
        return dp[n]
    
    for i in range(3, n + 1):
        dp.append(dp[i - 1] + dp[i - 2])
    
    return dp[-1] % 1234567
        
