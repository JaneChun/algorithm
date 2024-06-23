def solution(s):
    answer = []
    for i in range(len(s)):
        prevStr = s[0:i]
        idx = prevStr.rfind(s[i])
        if idx == -1:
            answer.append(idx)
        else:
            answer.append(i - idx)
    return answer