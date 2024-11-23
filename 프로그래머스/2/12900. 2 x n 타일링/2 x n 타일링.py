def solution(n):
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n + 1):
        dp[i] = (dp[i - 1] + dp[i - 2]) % 1000000007
    return dp[n]

# 1개 놓는 방법 : 1가지
# 2개 놓는 방법 : 2가지
# 3개 놓는 방법 : 1 + 2 = 3가지
# 4개 놓는 방법 : 2 + 3 = 5가지