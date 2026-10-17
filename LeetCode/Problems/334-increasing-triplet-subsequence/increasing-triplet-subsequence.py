# i < j < k && nums[i] < nums[j] < nums[k] 를 만족하면 true, 아니면 false 리턴
class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        if len(nums) < 3:
            return False

        first = nums[0] # 1
        second = float('inf')

        for i in range(1, len(nums)):
            if nums[i] < first: # first 교체, second 초기화
                first = nums[i]
            elif first < nums[i] < second: # second를 교체
                second = nums[i]
            elif first < second < nums[i]: # 조건 만족
                return True
            else: # 다음 i로 이동
                continue
        
        return False
            
        