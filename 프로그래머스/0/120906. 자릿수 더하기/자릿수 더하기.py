def solution(n):
    sum = 0
    string_n = str(n)
    for digit in string_n:
        sum += int(digit)
    return sum