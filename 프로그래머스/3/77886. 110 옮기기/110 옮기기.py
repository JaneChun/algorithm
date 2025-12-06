def solution(s):
    answer = []
    
    for string in s:
        stack = []
        count = 0
        
        # 모든 '110' 제거
        for char in string:
            stack.append(char)
            if len(stack) >= 3 and stack[-3:] == ['1', '1', '0']:
                stack.pop()
                stack.pop()
                stack.pop()
                count += 1
                
        remain = ''.join(stack)
        
        # 가장 마지막 '0'을 찾는다
        idx = remain.rfind('0')
        concatenated_110 = '110' * count
        
        # 0이 없다면 문자열 맨 앞에 넣고
        if idx == -1:
            answer.append(concatenated_110 + remain)
        # 있다면 마지막 0 뒤에 넣는다 -> 어떤 0이라도 앞에 110을 넣는다면 사전순 최적의 위치가 아니므로 마지막 0의 뒤에 배치하는게 최적이다
        else:
            left = remain[:idx+1]
            right = remain[idx+1:]
            answer.append(left + concatenated_110 + right)
            
    return answer