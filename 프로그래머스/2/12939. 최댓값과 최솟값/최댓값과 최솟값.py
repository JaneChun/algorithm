def solution(s):
    arr = [int(x) for x in s.split(' ')]
    
    return f"{min(arr)} {max(arr)}"