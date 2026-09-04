# 0 ~ n 을 담은 배열 nums가 주어졌을 때, 빠진 숫자를 찾아라
# 공간복잡도 O(1)와 시간복잡도 O(n)으로 풀어라

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        nums_set = set(nums)
        for i in range(n + 1):
            if i not in nums_set:
                return i

        