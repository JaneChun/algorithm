def solution(n):
    arr = [int(char) for char in str(n)]
    arr.sort(reverse=True)
    strArr = [str(num) for num in arr]
    return int(''.join(strArr))