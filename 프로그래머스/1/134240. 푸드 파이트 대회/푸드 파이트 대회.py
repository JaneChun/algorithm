import itertools

def solution(food):
    answer = '0'
    for i in range(len(food) - 1, 0, -1): # range(start, stop, step)
        count = int(food[i] / 2)
        for j in range(count):
            answer = str(i) + answer + str(i)
    return answer