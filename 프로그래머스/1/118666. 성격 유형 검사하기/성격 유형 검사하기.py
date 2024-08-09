def solution(survey, choices):
    answer = ''
    scores = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0}
    
    for i in range(len(survey)):
        A, B = survey[i]
        score = choices[i]
        
        if score < 4:
            scores[A] += 4 - score
        elif 4 < score:
            scores[B] += score - 4
    
    print(scores)
    # 키를 2개씩 쌍으로 묶음
    pairs = [('R', 'T'), ('C', 'F'), ('J', 'M'), ('A', 'N')]
    
    for A, B in pairs:
        if scores[A] > scores[B]:
            answer += A
        elif scores[A] < scores[B]:
            answer += B
        else:
            answer += A if A < B else B
        
    return answer