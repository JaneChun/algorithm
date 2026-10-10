# i + j + k = 0이되는 모든 조합을 찾기
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        answer = set()
        nums.sort() # O(nlogn)
        
        for i in range(len(nums) - 2):
            # i가 고정일 때 j, k를 이동시키며 합이 0이 되는 조합을 찾는다.
            j = i + 1
            k = len(nums) - 1

            while j < k:
                sum_of_3 = nums[i] + nums[j] + nums[k]
                if sum_of_3 == 0:
                    answer.add((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1
                elif sum_of_3 < 0:
                    j += 1
                else:
                    k -= 1

        return [list(x) for x in answer]
        