def solution(n):
    repeated = "수박" * int(n/2)
    return repeated if n % 2 == 0 else repeated + "수"