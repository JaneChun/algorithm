def solution(n):
    return "수박" * (n//2) + "수" * (n % 2)
    
    # repeated = "수박" * int(n/2)
    # return repeated if n % 2 == 0 else repeated + "수"