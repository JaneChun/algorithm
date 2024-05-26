from functools import reduce

def solution(num_list):
    if len(num_list) >= 11:
        return sum(num_list)
    else:
        return reduce(lambda acc, cur: acc * cur, num_list)