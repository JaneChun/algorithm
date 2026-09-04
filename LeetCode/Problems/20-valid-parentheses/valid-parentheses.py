# s를 순회하며 stack에 넣는다.
#   stack[-1]과 s[i]가 같다면 stack.pop

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(len(s)):
            cur = s[i]
            
            if len(stack) == 0:
                stack.append(cur)
            elif cur == ')' and stack[-1] == '(':
                stack.pop()
            elif cur == '}' and stack[-1] == '{':
                stack.pop()
            elif cur == ']' and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(cur)
        
        return len(stack) == 0
                
        