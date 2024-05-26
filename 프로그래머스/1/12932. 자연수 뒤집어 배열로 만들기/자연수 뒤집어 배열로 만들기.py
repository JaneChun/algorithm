def solution(n):
    arr = [char for char in str(n)]
    arr.reverse()
    return list(map(lambda x: int(x), arr))