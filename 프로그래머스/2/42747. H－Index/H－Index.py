def solution(citations):
    h_index = 0 # H-Index : 인용 횟수가 h 이상인 논문이 h편 이상일 때의 최댓값
    citations.sort(reverse = True)
    
    for i in range(len(citations)):
        if citations[i] >= i + 1:
            h_index += 1
    return h_index

