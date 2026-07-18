# shuffle - 배열을 섞어서 만들 수 있는 모든 순서가 동일한 확률로 나와야 한다
# 예를 들어 num = [1, 2, 3]일 때 가능한 수열은:
# [1, 2, 3]
# [1, 3, 2]
# [2, 1, 3]
# [2, 3, 1]
# [3, 1, 2]
# [3, 2, 1]
# 이 순열들이 각각 1/6 확률로 나와야한다.
class Solution:
    original: List[int]
    current: List[int]

    def __init__(self, nums: List[int]):
        self.original = nums[:]
        self.current = nums[:]

    def reset(self) -> List[int]:
        self.current = self.original[:]
        return self.current
        

    def shuffle(self) -> List[int]:
        # Fisher–Yates 셔플
            # 아직 확정되지 않은 범위에서 랜덤한 인덱스 j를 하나 고른다.
            # i와 j의 값을 교환한다.
            # 다음 인덱스로 이동한다.
            # 핵심은 랜덤 범위. 이미 확정한 0 ~ i-1 영역은 다시 건드리지 않는다.
        n = len(self.original)
        for i in range(n):
            j = random.randrange(i, n)
            self.current[i], self.current[j] = self.current[j], self.current[i]
        
        return self.current
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()