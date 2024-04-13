def solution(array, height):
    answer = 0
    for el in array:
        if el > height:
            answer += 1
    return answer