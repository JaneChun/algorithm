def solution(ingredient):
    count = 0
    stack = []
    
    for i in ingredient:
        if len(stack) < 3:
            stack.append(i)
        else:
            if i == 1 and stack[-1] == 3 and stack[-2] == 2 and stack[-3] == 1:
                count += 1
                for _ in range(3):
                    stack.pop()
            else:
                stack.append(i)

    
    return count
                
        