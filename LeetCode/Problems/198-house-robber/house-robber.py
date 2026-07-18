# nums = 각 집이 가지고 있는 금액 배열
# 제약: 인접한 집을 털 수 없음
# 최대 털 수 있는 금액을 리턴하라
class Solution:
    def rob(self, nums: List[int]) -> int:
        # 이전 집을 털었다면, 현재 집을 못 털고 (스킵)
        # 전전 집을 털었다면, 현재 집을 털 수 있음
        # dp[i] = max(dp[i - 2] + 현재 집, dp[i - 1])
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])

        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        max_money = nums[0]

        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
            max_money = max(max_money, dp[i])
        
        return max_money
