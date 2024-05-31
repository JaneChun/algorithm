def solution(numbers):
    arr = [0,1,2,3,4,5,6,7,8,9]
    return sum(0 if i in numbers else i for i in arr)