from functools import reduce

def solution(num_str):
    return sum(map(int, num_str))

    # arr = [int(char) for char in num_str];
    # return reduce(lambda acc, cur: acc + cur,arr)