def solution(k, m, score):
    score = sorted(score, reverse=True)
    boxes = []
    
    for i in range(0, len(score), m):
        if i + m - 1 < len(score):
            boxes.append(score[i:i + m])
    
    return sum([min(box) * m for box in boxes])