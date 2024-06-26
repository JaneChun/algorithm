def solution(k, score):
    answer = []
    
    hallOfFame = []
    for s in score:
        if len(hallOfFame) < k:
            hallOfFame.append(s) # [10, 100, 20]
        elif s > hallOfFame[-1]:
            hallOfFame.pop()
            hallOfFame.append(s)
        hallOfFame.sort(reverse=True)
        answer.append(hallOfFame[-1])
    
    return answer