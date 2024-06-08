def solution(n):
    reversedTernary = ""
    while n:
        reversedTernary += str(n % 3)
        n = n // 3
     
    return int(reversedTernary, 3)

    
    
    return result