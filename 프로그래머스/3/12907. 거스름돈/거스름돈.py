def solution(n, money):
    dp = [0] * (n + 1) # dp[i] = i를 만들 수 있는 방법의 개수
    
    for m in money:
        dp[m] += 1
        
        for i in range(n + 1):
            if i - m > 0 :
                dp[i] = (dp[i] + dp[i - m]) % 1000000007
    
    return dp[n]