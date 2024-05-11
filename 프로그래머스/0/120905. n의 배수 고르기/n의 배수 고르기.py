def solution(n, numlist):
    return list(filter(lambda num: num % n == 0, numlist));