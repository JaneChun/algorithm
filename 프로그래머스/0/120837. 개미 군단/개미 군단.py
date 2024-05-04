def solution(hp):
    generalAnt = int(hp / 5)
    hp = hp % 5
    
    soldierAnt = int(hp / 3)
    hp = hp % 3
    
    workerAnt = hp
    
    return generalAnt + soldierAnt + workerAnt