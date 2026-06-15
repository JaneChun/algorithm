# 세 숫자를 합쳐서 0이되는 모든 조합을 찾아서 리턴하라
# (-1, 0, 1) (0, 1, -1) 은 중복으로 친다
# 입력값이 최대 3000 -> O(N^3) = 27,000,000,000 (270억) X
# for 숫자 1개를 고정
    # 나머지 2개를 투포인터로
# -> O(N^2) = 9,000,000 -> O
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort() # [-4, -1, -1, 0, 1, 2]
        result = set()

        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1

            while j < k:
                sum = nums[i] + nums[j] + nums[k]
                
                if sum == 0:
                    result.add((nums[i], nums[j], nums[k]))
                    j += 1
                elif sum < 0:
                    j += 1
                else: # 0 < sum
                    k -= 1
        
        return list(map(list, result))