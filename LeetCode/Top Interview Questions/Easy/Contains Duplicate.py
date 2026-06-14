# 정수 배열 nums가 주어졌을 때, 배열에 같은 값이 두 번 이상 나타나면 true를 반환하고,
# 모든 원소가 서로 다르면 false를 반환하세요.

# Example 1:
# Input: nums = [1,2,3,1]
# Output: true
# 설명: 원소 1이 인덱스 0과 3에 나타납니다.

# Example 2:
# Input: nums = [1,2,3,4]
# Output: false
# 설명: 모든 원소가 서로 다릅니다.

# Example 3:
# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true

# 제약 조건:
# 1 <= nums.length <= 10^5
# -10^9 <= nums[i] <= 10^9

import sys

input = sys.stdin.readline

nums = list(map(int, input().split(",")))

unique_nums = set(nums)
print(len(unique_nums) != len(nums))
