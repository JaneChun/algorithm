# prices[i]는 i번째 날의 주식의 가격
# 한 번 사고 다른 날에 팔아서 최대 수익이 되는 수익을 찾아라
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = [None] * len(prices) # memo[i]는 이전 일자(0 ~ i - 1) 중에 가장 싼 가격
        memo[0] = prices[0]
        max_profit = 0

        # O(N)
        for i in range(1, len(prices)):
            cheapest = min(memo[i - 1], prices[i - 1]) # 이전 값과 비교해서 더 싼 가격 갱신
            memo[i] = cheapest

            profit = prices[i] - cheapest
            max_profit = max(max_profit, profit)

        return max_profit
        
