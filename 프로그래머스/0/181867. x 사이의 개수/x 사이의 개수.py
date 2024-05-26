def solution(myString):
    arr = myString.split('x')
    return list(map(lambda str: len(str), arr))