def solution(n):
    n3 = to_base(n, 3)
    reversed_n3 = str(n3)[::-1]
    return int(reversed_n3, 3)

def to_base(n, base):
    result = ""
    while n:
        result = str(n % base) + result
        n = n // base # 몫
    
    return result