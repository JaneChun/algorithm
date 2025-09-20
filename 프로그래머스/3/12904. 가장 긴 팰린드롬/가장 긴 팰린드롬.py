def solution(s):
    max_len_1 = 0
    max_len_2 = 0
    
    for i in range(0, len(s)):
        length = 0
        center = s[i]
        
        # s[i - length] = left
        # s[i + length] = right
        while (0 <= i - length and i + length < len(s) and s[i - length] == s[i + length]):
            length += 1
            
        max_len_1 = max(max_len_1, (length * 2) - 1)
        
    for i in range(0, len(s) - 1):
        length = 0
        center_left = s[i]
        center_right = s[i + 1]
        
        if center_left != center_right:
            continue
        
        # s[i - length] = left
        # s[i + 1 + length] = right
        while (0 <= i - length and i + 1 + length < len(s) and s[i - length] == s[i + 1 + length]):
            length += 1
            
        max_len_2 = max(max_len_2, length * 2)

    return max(max_len_1, max_len_2)