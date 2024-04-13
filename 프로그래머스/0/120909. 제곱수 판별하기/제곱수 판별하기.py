import math

def solution(n):
    answer = 0
    sqrt = math.sqrt(n) # float형
    if sqrt.is_integer():
        answer = 1
    else:
        answer = 2
    return answer