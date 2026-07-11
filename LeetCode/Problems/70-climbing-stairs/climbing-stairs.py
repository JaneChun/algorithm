# n칸까지 가야하고, 한 번에 1칸 또는 2칸씩 올라갈 수 있다.
# n까지 가는 몇가지 방식이 있는가?
class Solution:
    def climbStairs(self, n: int) -> int:
        # dp[i] = i칸까지 가는 방법의 수
        # dp[1] = 1
        # dp[2] = 2
        # dp[3] = dp[3-1] + dp[3-2] -> 3칸까지 오려면 2칸에서 1칸을 올라오거나, 1칸에서 2칸을 올라와야 함
        # dp[4] = dp[4-1] + dp[4-2]
        # dp[i] = dp[i-1] + dp[i-2] -> i칸까지 오는 방법의 수: i-1칸에서 1칸을 올라온 방법의 수 + i-2칸에서 2칸을 올라온 방법의 수
        if n == 1:
            return 1
        if n == 2:
            return 2
            
        dp = [None] * (n + 1) # 1-based
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n + 1):
            dp[i] = dp[i-1] + dp[i-2]

        return dp[n]