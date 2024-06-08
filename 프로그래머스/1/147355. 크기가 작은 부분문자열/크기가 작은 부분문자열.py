def solution(t, p):
    answer = 0
    for i in range(len(t) - len(p) + 1):
        sliced = t[i:i + len(p)]
        if int(sliced) <= int(p):
            answer += 1
    return answer