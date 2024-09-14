def solution(n):
    battery = 0
    
    while n > 0:
        if n % 2 == 0:
            n /= 2
            continue
        else:
            k = n % 2
            battery += k
            n -= k

    return battery
