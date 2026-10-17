# 투 포인터, 슬라이딩 윈도우
# n = 100,000 이므로 O(n) -> 100,000
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        char_set = set()
        left = 0
        right = 0

        while left <= right < len(s):
            # 새로운 문자(right)가 중복이 아니라면, set에 추가하고 길이를 갱신한다.
            if s[right] not in char_set:
                char_set.add(s[right])
                length = right - left + 1
                max_length = max(max_length, length)
            # 새로운 문자(right)가 중복이라면, 현재 문자열에서 중복된 문자 + 1 까지 left 포인터를 옮긴다.
            else: 
                while s[left] != s[right]:
                    char_set.remove(s[left])
                    left += 1
                left += 1
            right += 1

        return max_length