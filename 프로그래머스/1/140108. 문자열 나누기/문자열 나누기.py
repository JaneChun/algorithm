def solution(s):
    answer = []
    
    char = s[0]
    startIdx = 0
    sameCnt = 0
    otherCnt = 0
    
    for i in range(len(s)):
        if i == len(s) - 1: # 마지막 요소인 경우 그냥 추가
            return len(answer) + 1
        
        if s[i] == char:
            sameCnt += 1
        else :
            otherCnt += 1
        
        if sameCnt == otherCnt:
            answer.append(s[startIdx: i + 1])
            sameCnt = 0
            otherCnt = 0
        
            if i + 1 < len(s):
                char = s[i + 1] # prev값 갱신
                startIdx = i + 1 # startIdx 갱신
    print(answer)
    return len(answer)