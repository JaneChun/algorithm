def isRightBracketString(s):
    stack = []
    
    for bracket in s:
        if bracket in ['[', '{', '(']:
            stack.append(bracket)
        elif bracket in [']', '}', ')']:
            if not stack:
                return False
            
            top = stack[-1]
            if (top == '[' and bracket == ']') or \
               (top == '{' and bracket == '}') or \
               (top == '(' and bracket == ')'):
                stack.pop() 
        else:
            return False
    return len(stack) == 0

def solution (s):
    count = 0
    for i in range(len(s)):
        if isRightBracketString(s):
            count += 1
        s = s[1:] + s[0]
            
    return count