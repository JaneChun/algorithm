def solution(arr, n):
    if len(arr) % 2 == 0:
        return list(map(lambda i, num: num + n if i % 2 == 1 else num, range(len(arr)), arr))
    else:
        return list(map(lambda i, num: num + n if i % 2 == 0 else num, range(len(arr)), arr))
    