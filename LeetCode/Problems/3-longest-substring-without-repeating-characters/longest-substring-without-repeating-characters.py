# 문자열 s에서 중복되는 문자 없이 가장 긴 부분 문자열을 찾고 그 길이를 반환하라
# 문자열의 길이는 50,000 이므로 O(N^2) = 2,500,000,000 (250억) X
# 슬라이딩 윈도우로 O(N)에 풀어야 함
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        char_set = set()
        answer = 0

        for right in range(len(s)):
            # right을 1씩 증가시키면서
            # char_set에 s[right]을 추가한다.
            if s[right] not in char_set:
                char_set.add(s[right])
                answer = max(answer, len(char_set))
            else: 
                # 중복이 나온 경우
                # left을 1씩 증가시키면서
                # char_set에서 s[left]를 제거한다.
                while s[right] in char_set:
                    char_set.remove(s[left])
                    left += 1
                
                char_set.add(s[right])
                answer = max(answer, len(char_set))
            
        return answer