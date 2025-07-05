def solution(n, s):
    if s < n:
        return [-1]
    
    mod = s // n # 4
    rest = s % n # 1
    
    result = [mod] * n # [4, 4]

    for i in range(n - 1, n - 1 -rest, -1): # 나머지만큼
        result[i] += 1 # 뒤쪽에서 1씩 더하기

    return result