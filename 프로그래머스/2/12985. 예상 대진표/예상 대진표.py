import math

def solution(n,a,b):
    round = 0
    
    if a > b:
        a, b = b, a
    
    while a < b:
        a = math.ceil(a / 2)
        b = math.ceil(b / 2)
        round += 1

    return round

# 1 2 3 '4' 5 6 '7' 8

# 1 '2' 3 '4'

# '1' '2'

# '1'