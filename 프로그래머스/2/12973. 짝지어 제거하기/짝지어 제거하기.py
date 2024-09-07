# 시간 초과
# def solution(s):
#     while True:
#         modified = False

#         for i in range(len(s) - 1):
#             if s[i] == s[i + 1]:
#                 s = s[:i] + s[i + 2:]
#                 modified = True
#                 break
                
#         if not modified: # 문자열을 모두 순회할 동안 수정되지 않은 경우 while문 탈출
#             break

#     return 0 if len(s) else 1
        
def solution(s):
    stack = []
    for char in s:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)
        
    return 1 if len(stack) == 0 else 0