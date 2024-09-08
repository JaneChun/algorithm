def solution(bandage, health, attacks):
    [t, x, y] = bandage
    heal_time = 0    
    max_health = health
    last_attack_time = attacks[-1][0]
    
    for time in range(0, last_attack_time + 1):
        [attackTime, damage] = attacks[0]
        
        if time == attackTime:
            attacks.pop(0)
            health -= damage # 피깎
            heal_time = 0
            if health <= 0: # 사망
                return -1
            continue
    
        health += x
        heal_time += 1
        
        if heal_time == t:
            health += y
            heal_time = 0
            
        if health > max_health:
            health = max_health
            
    return health