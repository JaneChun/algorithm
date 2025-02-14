def solution(n):
    answer = []
    
    def hanoi(n, start, end, via):
        if n == 1:
            answer.append([start, end])
            return
        hanoi(n - 1, start, via, end) # n - 1개를 via에 옮겨두고
        answer.append([start, end]) # 가장 큰 원판 이동
        hanoi(n - 1, via, end, start) # n - 1개도 end로 이동
        
    hanoi(n, 1, 3, 2)
    return answer