import math

def solution(n, k):
    answer = 0
    
    transformed = to_base(n, k)
    arr = transformed.split('0')

    for item in arr:
        if item != '':
            if is_prime(int(item)):
                answer += 1
    
    return answer

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    
    return True
    

def to_base(n, k):
    if n == 0:
        return "0"
    
    digits = []
    
    while n:
        digits.append(str(n % k))
        n //= k
    
    return ''.join(digits[::-1])