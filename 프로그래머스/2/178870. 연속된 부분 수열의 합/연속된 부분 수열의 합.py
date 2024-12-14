def solution(sequence, k):
    answer = []
    
    curSum = 0
    left = 0
    right = 0
    minLength = len(sequence)
    
    for right in range(len(sequence)): # right이 끝까지 갈 때까지
        curSum += sequence[right]
        
        while k < curSum:
            curSum -= sequence[left]
            left += 1
            
        # 현재 부분 수열의 합이 k와 같을 때
        if k == curSum:
            if right - left < minLength: # 이전 발견한 수열 보다 길이가 짧은 경우에만 갱신
                minLength = right - left
                answer = [left, right]
    return answer