def solution(n):
    battery = 0
    
    while n > 0:
        if n % 2 == 0:
            n /= 2
            continue
        else:
            battery += n % 2
            n = n // 2

    return battery
