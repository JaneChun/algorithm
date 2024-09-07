def solution(n):
    next_n = n + 1
    while True:
        if bin(next_n).count('1') == bin(n).count('1'):
            return next_n
        else:
            next_n += 1