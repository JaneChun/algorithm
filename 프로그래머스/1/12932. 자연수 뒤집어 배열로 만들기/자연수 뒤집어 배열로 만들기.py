def solution(n):
    arr = list(str(n))
    arr.reverse()
    return list(map(lambda x: int(x), arr))