def solution(rsp):
    answer = ''
    for hand in rsp:
        if hand == "2":
            answer += "0"
        elif hand == "5":
            answer += "2"
        else:
            answer += "5"
    return answer