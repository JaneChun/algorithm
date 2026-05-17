# https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/879/

# 문자열을 뒤집는 함수를 작성하세요. 입력 문자열은 문자 배열 s로 주어집니다.
# 입력 배열을 제자리에서 수정해야 하며, 추가 메모리는 O(1)만 사용해야 합니다.

# 예시 1:
# Input: s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]

# 예시 2:
# Input: s = ["H","a","n","n","a","h"]
# Output: ["h","a","n","n","a","H"]

# 제약 조건:
# 1 <= s.length <= 10^5
# s[i]는 출력 가능한 ASCII 문자입니다.


import sys

input = sys.stdin.readline

s = input().replace("[", "").replace("]", "").replace('"', "").split(",")

# 메모리를 O(1)만 사용해야 한다 = 입력 크기 n에 비례하는 새 배열/자료구조를 만들지 말고, 기존 arr 자체를 수정하라는 뜻

left = 0
right = len(s) - 1

while left < right:  # 둘이 같아질 때까지
    s[left], s[right] = s[right], s[left]
    left += 1
    right -= 1

print(s)
