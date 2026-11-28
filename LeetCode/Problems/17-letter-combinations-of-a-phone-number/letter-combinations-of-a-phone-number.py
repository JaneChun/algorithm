class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        def backtrack(string):
            if len(string) == len(digits): # 글자수가 다 차면 result에 추가하고 재귀 호출 종료
                result.append(string)
                return

            number = digits[len(string)] # "2" # "3"
            for char in digit_to_letters[number]: # "abc"  # "def"
                backtrack(string + char) # "a"               "b" 
                                         # "ad" "ae" "af"    "bd" "be" "bf"
        result = []

        digit_to_letters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        backtrack("")


        return result
        
# 시간복잡도
# digits의 길이 n, digit 하나당 최대 4개의 조합이므로
# O(n * 4^n) 예를들어 n = 2인 경우 2자리 2 * (4*4) = 32