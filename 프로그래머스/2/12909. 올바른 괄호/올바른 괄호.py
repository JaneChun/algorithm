def solution(s):
    stack = []
    
    for bracket in s:
        if bracket == '(': # 왼쪽 괄호를 만나면 스택에 넣는다.
            stack.append(bracket)
        else:
            if stack: # 오른쪽 괄호를 만나면 스택을 pop 한다.
                stack.pop()
            else:
                return False # 스택이 비어있는 경우 바로 False 리턴
    
    return len(stack) == 0
        
            