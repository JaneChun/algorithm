def solution(answers):
    counts = [0, 0, 0, 0]
    supojas = [
        [1, 2, 3, 4, 5], 
        [2, 1, 2, 3, 2, 4, 2, 5], 
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ]
    for i in range(len(answers)):
        for j in range(len(supojas)):
            supoja_answer = supojas[j]
            if supoja_answer[i % len(supoja_answer)] == answers[i]:
                counts[j + 1] += 1
    
    maxCount = max(counts)
    return sorted([i for i, x in enumerate(counts) if x == maxCount])
        
                
                
            