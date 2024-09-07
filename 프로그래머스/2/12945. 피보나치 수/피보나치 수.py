# def solution(n):
#     def fibo(i):
#         if i == 0:
#             return 0
#         elif i == 1:
#             return 1
#         else:
#             return fibo(i - 2) + fibo(i - 1)
    
#     return fibo(n) % 1234567
# 1. 시간 복잡도가 O(2^n) 
# 2. 재귀 호출이 많이 쌓여서 스택 오버플로우로 인한 런타임 에러 발생

# def solution(n):
#     dp = [0, 1]
#     for i in range (2, n + 1):
#         dp.append(dp[i - 2] + dp[i - 1])
#     return dp[-1]
# n의 값이 커질수록 메모리 부족 또는 큰 수 처리로 인한 런타임 에러 발생

# 모듈러 연산 (a+b)%m=((a%m)+(b%m))%m
def solution(n):
    dp = [0, 1]
    for i in range (2, n + 1):
        dp.append((dp[i - 2] + dp[i - 1]) % 1234567)
    return dp[-1]
