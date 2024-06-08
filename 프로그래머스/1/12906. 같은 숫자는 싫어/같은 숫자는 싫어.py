def solution(arr):
    answer = []
    for n in arr:
        # if len(answer) == 0 or n != answer[-1]:
        if not answer or n != answer[-1]:
            answer.append(n)
    return answer