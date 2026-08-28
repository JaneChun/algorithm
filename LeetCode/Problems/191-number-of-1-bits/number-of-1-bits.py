class Solution:
    def hammingWeight(self, n: int) -> int:
        answer = ''
        while n > 1: # n = 0 또는 1이 될 때 까지
            r = n % 2
            n //= 2
            answer = str(r) + answer
        
        # 마지막 1 더해주기
        answer = str(1) + answer

        return answer.count('1')

        