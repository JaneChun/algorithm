def solution(strArr):
    return list(map(lambda x: x[1].upper() if x[0] % 2 == 1 else x[1].lower(), enumerate(strArr))) # x[0] : 인덱스, x[1] : 요소