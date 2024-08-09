def solution(new_id):
    answer = new_id.lower()
    answer = ''.join([x for x in answer if x.isalpha() or x.isdigit() or x in['-', '_', '.']])
    while '..' in answer:
        answer = answer.replace('..', '.')
    answer = answer.strip('.')
    if len(answer) == 0:
        answer = 'a'
    if len(answer) >= 16:
        answer = answer[:15]
    answer = answer.rstrip('.')
    if len(answer) <= 2:
        char = answer[-1]
        answer += char * (3 - len(answer))
    return answer