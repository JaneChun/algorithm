# 두 정수 사이의 hamming distance는 일치하는 비트가 다른 자리의 수를 말한다.
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        distance = 0

        x_bin = self.get_binary(x)
        y_bin = self.get_binary(y)
        print(x_bin, y_bin)

        bin_len = max(len(x_bin), len(y_bin))
        padded_x_bin = x_bin.zfill(bin_len)
        padded_y_bin = y_bin.zfill(bin_len)

        print(padded_x_bin, padded_y_bin)

        for i in range(bin_len):
            if padded_x_bin[i] != padded_y_bin[i]:
                distance += 1
            
        return distance
        
    def get_binary(self, n: int) -> str:
        answer = ''

        if n == 0:
            return '0'

        while n > 1:
            r = n % 2
            n //= 2
            answer = str(r) + answer
        
        answer = str(1) + answer

        return answer

        