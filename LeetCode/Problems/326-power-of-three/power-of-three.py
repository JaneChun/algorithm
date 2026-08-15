# n은 최대 21.5억
# 1,3,9,27,…,3^k이므로 3^k≤n인 동안 반복한다.
# 따라서 최대 반복 횟수는 k≈log3n이고, 시간 복잡도는 O(log n) 이다.
# 최악의 경우 n = 2^31 일 때, log^3(2^31) ≈ 19.56 (20회의 연산)
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        
        x = 1
        while x < n:
            x *= 3
        
        return x == n