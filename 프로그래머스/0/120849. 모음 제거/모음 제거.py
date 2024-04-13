def solution(my_string):
    answer = my_string
    for vowel in ['a', 'e', 'i', 'o', 'u']:
        answer = answer.replace(vowel, '')
    return answer