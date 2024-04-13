def solution(numbers):
    answer = 0
    max_value = max(numbers)
    numbers.remove(max_value)
    second_max_value = max(numbers)
    return max_value * second_max_value