def solution(s):
    max_len_1 = 0 # 중심이 1글자인 경우
    max_len_2 = 0 # 중심이 2글자인 경우
    
    for i in range(0, len(s)):
        length = 0
        left = i
        right = i
        
        while (0 <= left and right < len(s) and s[left] == s[right]):
            length += 1
            left = i - length
            right = i + length
            
        max_len_1 = max(max_len_1, (length * 2) - 1)
        
    for i in range(0, len(s) - 1):
        length = 0
        left = i
        right = i + 1
        
        if s[left] != s[right]:
            continue
        
        while (0 <= left and right < len(s) and s[left] == s[right]):
            length += 1
            left = i - length
            right = i + 1 + length
            
        max_len_2 = max(max_len_2, length * 2)

    return max(max_len_1, max_len_2)