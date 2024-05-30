import math

def solution(n):
    sqrt = int(math.sqrt(n))
    isInteger = sqrt * sqrt == n
    
    if isInteger:
        return (sqrt + 1) * (sqrt + 1)
    else:
        return -1