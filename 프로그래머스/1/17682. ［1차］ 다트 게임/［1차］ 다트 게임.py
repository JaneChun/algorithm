import re

def solution(dartResult):
    answer = []
    result = re.findall(r'(\d{1,2})([SDT])([*#])?', dartResult)
    # [('1', 'S', ''), ('2', 'D', '*'), ('3', 'T', '')]
    
    for score, bonus, option in result:
        score = int(score)
        
        if bonus == 'S':
            score = score ** 1
        elif bonus == 'D':
            score = score ** 2
        elif bonus == 'T':
            score = score ** 3
            
            
        if option == '*':
            score *= 2
            if len(answer): 
                answer[-1] *= 2
        elif option == '#':
            score *= -1
            
        answer.append(score)
    
    return sum(answer)