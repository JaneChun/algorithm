def solution(a, b, n):
    answer = 0
    while n >= a:
        extra = n // a
        n -= a * extra
        n += b * extra
        answer += b * extra
        
    return answer