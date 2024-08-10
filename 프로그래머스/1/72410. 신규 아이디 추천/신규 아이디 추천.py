def solution(new_id):
    #1
    answer = new_id.lower()
    #2
    answer = ''.join([x for x in answer if x.isalpha() or x.isdigit() or x in['-', '_', '.']])
    #3
    while '..' in answer:
        answer = answer.replace('..', '.')
    #4
    answer = answer.strip('.')
    #5
    if len(answer) == 0:
        answer = 'a'
    #6
    if len(answer) >= 16:
        answer = answer[:15]
    answer = answer.strip('.')
    #7
    if len(answer) <= 2:
        char = answer[-1]
        answer += char * (3 - len(answer))
    return answer