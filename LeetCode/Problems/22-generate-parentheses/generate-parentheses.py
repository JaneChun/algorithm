class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        result = []

        def backtrack(string, open, close):
            length = len(string)

            if length == 2 * n:
                result.append(string)
                return

            # open을 넣을 수 있는 조건: 최대 n개까지는 가능 (모두 열고 모두 닫는 조합)
            if open < n:
                backtrack(string + '(', open + 1, close)
            # close를 넣을 수 있는 조건: close의 개수가 open보다 작을 때 (close가 더 많거나 같으면 이미 well-formed가 아님)
            if close < open:
                backtrack(string + ')', open, close + 1)

        backtrack("(", 1, 0)

        return result