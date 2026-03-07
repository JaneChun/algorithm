import sys

n = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split(" ")))

dp = [1] * n

for i in range(1, n):
    prev_max = 1  # i 앞의 j 들 중 최대 연속 횟수를 찾아 dp[j]+1 해서 dp[i]에 갱신한다.
    for j in range(i):
        if numbers[j] < numbers[i]:  # i < j
            prev_max = max(prev_max, dp[j] + 1)
    dp[i] = prev_max

print(max(dp))