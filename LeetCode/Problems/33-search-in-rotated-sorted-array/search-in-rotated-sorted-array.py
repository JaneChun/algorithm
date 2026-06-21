# nums = 각기 다른 값의 정수 배열(오름차순)
# nums 배열은 k(0-indexed) 값에 의해 left-rotated된 상태이다.
# 원본: [0,1,2,4,5,6,7]
# k = 3만큼 회전 (k는 알 수 없음)
# nums = [4,5,6,7,0,1,2]
# 회전된 nums와 정수 target을 받아, target이 nums에 있다면 그 인덱스를 반환하고, 없다면 -1을 반환하라
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # O(N)
        # return nums.index(target) if target in nums else -1

        # O(log N) -> 이진탐색
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target: # target을 찾았다면
                return mid # 인덱스를 반환한다.

            # target 찾는 법
            # mid를 기준으로 왼쪽 구간과 오른쪽 구간 중 하나는 무조건 정렬되어 있다.
            # e.g. [4,5,6] [7,0,1,2]
            
            # 정렬된 구간을 찾고, 그 안에 target이 있다면 이 범위로 좁혀서 이분 탐색을 이어서 진행

            # 왼쪽 구간이 정렬되어 있는 경우
            if nums[left] <= nums[mid]:
                # 이 구간 안에 target이 있다면, 이 범위에서 다시 이분 탐색
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else: # target이 없다면, 오른쪽 구간을 탐색
                    left = mid + 1
            # 오른쪽 구간이 정렬되어 있는 경우
            else:
                print('오른쪽 구간이 정렬됨')
                # 이 구간 안에 target이 있다면, 이 범위에서 다시 이분 탐색
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else: # target이 없다면, 왼쪽 구간을 탐색
                    right = mid - 1
        
        return -1