# n = 1,000 이므로 O(n^2) -> 1,000,000
class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_length = 1
        index = [0, 0]

        # i가 중심일 때, i, i+1 이 중심일 때 양쪽으로 뻗어나가며 팰린드롬인지 확인하고 끊기는 경우 길이 갱신
        for i in range(len(s)):
            # 홀수
            for j in range(1, len(s)): # j = 중심으로부터의 거리
                if not (0 <= i - j and i + j < len(s)): # 범위 내인지 체크
                    break
                if s[i - j] == s[i + j]: # 양쪽이 같은지 체크
                    length = j * 2 + 1

                    if max_length < length:
                        max_length = length
                        index = [i - j, i + j]
                else:
                    break
            # 짝수
            for j in range(0, len(s)):
                if not (0 <= i - j and i + 1 + j < len(s)):
                    break
                if s[i - j] == s[i + 1 + j]:
                    length = j * 2 + 2

                    if max_length < length:
                        max_length = length
                        index = [i - j, i + 1 + j]
                else:
                    break
        
        return s[index[0]:index[1] + 1]
