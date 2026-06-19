# 양의 정수 nums, target
# target보다 크거나 같은 부분 배열의 최소 길이를 리턴하라
# 조건을 만족하는 부분 배열이 없는 경우 0을 리턴하라

# 현재 풀이의 시간복잡도는 슬라이딩 윈도우를 사용했으나 최악의 경우 O(N^2)
# 10,000(window size) * 10,000(nums) = 100,000,000 (1억)
# class Solution:
#     def minSubArrayLen(self, target: int, nums: List[int]) -> int:
#         window_sum = [] # 초기값
#         for w in range(1, len(nums) + 1): # w: 윈도우의 크기
#             num_sum = sum(nums[:w]) # 초기합

#             if num_sum >= target:
#                 return w

#             for start in range(1, len(nums) - w + 1):
#                 end = start + w - 1
#                 num_sum -= nums[start - 1] # 이전 값을 빼고
#                 num_sum += nums[end] # 다음 값 추가
#                 if num_sum >= target:
#                     return w
        
#         return 0

# =========================================
# 가변 길이 슬라이딩 윈도우 -> O(N)
# 슬라이딩 윈도우의 크기를 지정하지 않고 left, right 포인터만 사용한다.
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        right = 0
        num_sum = nums[left] # 초기값

        possible_cases = []

        while left <= right and right < len(nums):
            if target <= num_sum:
                window_size = right - left + 1
                possible_cases.append(window_size)

                num_sum -= nums[left]
                left += 1

            else: # target > num_sum
                right += 1
                if right < len(nums):
                    num_sum += nums[right]

        return min(possible_cases) if len(possible_cases) else 0