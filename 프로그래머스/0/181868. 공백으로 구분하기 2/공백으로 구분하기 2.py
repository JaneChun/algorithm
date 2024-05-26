def solution(my_string):
    arr = my_string.split(' ')
    return list(filter(lambda str: str.strip(), arr))