# nums 배열에서 가장 합이 큰 부분 배열을 찾고 그 합을 리턴하라
# O(N) -> 카데인 알고리즘
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # dp[i] = i까지의 최대 부분합
        # dp[i] = max(현재 노드, dp[i - 1] + 현재 노드) -> 현재값부터 다시 시작하거나, 누적값에 현재값을 더하거나 -> 둘 중 큰 값
        dp = [-float('inf')] * len(nums)
        dp[0] = nums[0]
        max_sum = nums[0]
        
        for i in range(1, len(nums)):
            dp[i] = max(nums[i], dp[i - 1] + nums[i])
            max_sum = max(max_sum, dp[i])

        return max_sum



        