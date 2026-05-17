# https://leetcode.com/explore/interview/card/top-interview-questions-easy/96/sorting-and-searching/587/

# 정수 배열 nums1과 nums2가 주어집니다.

# 두 배열은 모두 오름차순 정렬되어 있습니다.

# 또한 정수 m과 n이 주어지며, 각각 다음을 의미합니다.
# m: nums1에 실제로 들어 있는 원소의 개수
# n: nums2에 들어 있는 원소의 개수

# nums1과 nums2를 하나의 배열로 합치되, 결과 배열도 오름차순으로 정렬되어 있어야 합니다.

# 최종 정렬된 배열을 함수에서 return하면 안 됩니다.
# 대신 결과를 nums1 배열 안에 직접 저장해야 합니다.

# 결과적으로 nums1의 길이는 m + n입니다.

# nums1의 앞쪽 m개 원소는 실제 병합해야 하는 값입니다.
# nums1의 뒤쪽 n개 원소는 0으로 채워져 있으며, 이 값들은 무시해야 합니다.
# nums2의 길이는 n입니다.

# Example 1:
# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]

# Example 2:
# Input: nums1 = [1], m = 1, nums2 = [], n = 0
# Output: [1]

# Example 3:
# Input: nums1 = [0], m = 0, nums2 = [1], n = 1
# Output: [1]
# Explanation: The arrays we are merging are [] and [1].
# 주의할 점은 m = 0이기 때문에 nums1에는 실제 원소가 없습니다.
# nums1에 있는 0은 병합 결과를 저장할 공간을 확보하기 위해 있는 값일 뿐입니다.

# Constraints:
# nums1.length == m + n
# nums2.length == n
# 0 <= m, n <= 200
# 1 <= m + n <= 200
# -109 <= nums1[i], nums2[j] <= 109

# Follow up: Can you come up with an algorithm that runs in O(m + n) time?

import sys

input = sys.stdin.readline

nums1 = list(map(int, input().split(",")))
m = int(input())
nums2 = list(map(int, input().split(",")))
n = int(input())

# nums1 = [1, 2, 3, 0, 0, 0]
#                i        k
# m = 3
# nums2 = [2, 5, 6]
#                j
# n = 3

# 새로운 배열을 만들지 말고 nums1를 업데이트해야 함
# O(m + n)으로 풀려면..

# 포인터를 3개 사용
# nums1의 실제 마지막 원소 위치: m - 1
# nums2의 마지막 원소 위치: n - 1
# nums1에 값을 넣을 위치: m + n - 1

i = m - 1
j = n - 1
k = m + n - 1

# k에 nums1의 가장 큰 수(i)와 nums2의 가장 큰 수(j) 중 더 큰 수를 넣는다
# k -= 1
# 반복..

for k in range(m + n - 1, -1, -1):
    if j < 0:  # nums2에 더 이상 요소가 없으면 종료 (nums1는 이미 정렬된 상태)
        break

    # i >= 0 조건을 추가해야하는 이유: i를 다 사용했다면 무조건 nums2[j]를 넣어야 하므로
    if i >= 0 and nums1[i] > nums2[j]:
        nums1[k] = nums1[i]
        i -= 1
    else:
        nums1[k] = nums2[j]
        j -= 1

print(nums1)

# i = 2
# j = 2
# k = 5

# for k in range(6, 0, -1)
#
