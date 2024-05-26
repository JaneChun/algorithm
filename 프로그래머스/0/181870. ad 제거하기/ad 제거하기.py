def solution(strArr):
    return list(filter(lambda str: 'ad' not in str, strArr))