# 물을 많이 가두는 2개의 라인 찾고
# 물의 면적 리턴하기
# 라인은 최대 10,000개 이므로 O(N^2) = 100,000,000 (1억) X
# 투포인터 O(N)으로 풀기
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_water = 0

        while left < right:
            width = right - left
            min_height = min(height[left], height[right])
            max_water = max(max_water, width * min_height)

            # 언제 left += 1을 하고
            # 언제 right -= 1을 할까?

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_water

        
        