# input을 이진수로 바꾸고 reverse한 후 다시 십진수로 반환한다.
class Solution:
    def reverseBits(self, n: int) -> int:
        answer = 0
        n_bin = self.int_to_32_bit(n)
        
        # bin to str
        # 앞에서부터 2^0, 2^1, 2^2 ... 를 곱한다.
        for i in range(len(n_bin)):
            answer += int(n_bin[i]) * (2 ** i)
        
        return answer

    def int_to_32_bit(self, n: int) -> str:
        return str(bin(n))[2:].zfill(32)
