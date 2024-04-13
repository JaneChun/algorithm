def solution(my_string):
    answer = ''
    
    for char in my_string:
        answer = char + answer
        
    return answer