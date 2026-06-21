# amount를 만들기 위한 최소한의 동전 개수를 사용하는 조합을 찾고, 그 최소 개수를 리턴하라
# 어떤 조합으로도 amount를 만들 수 없는 경우 -1을 리턴하라
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # 큰 동전을 많이 쓰는 것이 항상 최소의 수가 되지 않음 -> 그리디 접근 실패
        # e.g. coins = [1, 3, 4], amount = 6 / 정답: 2, 내 풀이: 3

        # coins.sort(reverse=True)
        # total_count = 0

        # for i in range(len(coins)):
        #     coin = coins[i]
        #     count = amount // coin
        #     amount = amount - coin * count
        #     total_count += count
        
        # return total_count if amount == 0 else -1
        

        # dp 풀이
        # dp[i] = 금액 i를 만들기 위한 동전의 최소 개수
        # e.g. coins = [1,2,5], amount = 11
            # dp[0] = 0
            # dp[1] = 1
            # dp[2] = 1
            # dp[5] = 1
            # ...
            # dp[i] = min(dp[i - 1] + 1, dp[i - 2] + 1, dp[i - 5] + 1)
        
        dp = [float('inf')] * (amount + 1) # 1-based-index
        dp[0] = 0
        
        for i in range(1, amount + 1): # dp[amount] 까지 할당해야하므로
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        
        return -1 if dp[amount] == float('inf') else dp[amount]