# n은 최대 21.5억
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        
        x = 1
        while x < n:
            x *= 3
        
        return x == n