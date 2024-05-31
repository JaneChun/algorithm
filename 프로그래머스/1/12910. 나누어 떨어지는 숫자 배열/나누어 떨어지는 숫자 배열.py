def solution(arr, divisor):
    filtered = list(filter(lambda x: x % divisor == 0, arr))
    return sorted(filtered) if len(filtered) else [-1]
    