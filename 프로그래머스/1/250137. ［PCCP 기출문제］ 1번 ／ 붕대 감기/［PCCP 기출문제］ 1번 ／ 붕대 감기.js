function solution(bandage, health, attacks) {
    const [t, x, y] = bandage
    let currentHealth = health
    let currentAttack = attacks.shift()
    
    let healCount = 0
    const lastAttackTime = attacks.at(-1)[0]
    for (let time = 1; time <= lastAttackTime; time++) {
        const [attackTime, damage] = currentAttack
        
        if (attackTime === time) {
            // 공격 받음
            currentHealth -= damage
            if (currentHealth <= 0) return -1
            healCount = 0 // 공격 받을 시 연속 성공 초기화
            
            if (attacks.length) currentAttack = attacks.shift()
        } else {
            // 붕대 감기
            if (currentHealth >= health) continue // 최대 체력이면 안감음
            else {
                currentHealth += x // 초당 x씩 회복
                healCount++
                if (healCount === t) {
                    currentHealth += y // 연속 회복 성공 시 추가 회복
                    healCount = 0 // 연속 성공 초기화
                }
                // 회복이 끝나고, 최대 체력을 초과했으면 최대 체력으로 바꿔줌
                if (currentHealth > health) currentHealth = health
            }
        }
        console.log('time', time, 'currentHealth', currentHealth)
    }
    return currentHealth > 0 ? currentHealth : -1
}

// 붕대 감는 데 걸리는 시간 t초
// 감는동안 1초마다 x만큼 회복
// 다 감으면 y만큼 추가 회복

// 공격 당하면 취소
// 0초로 초기화

solution([5, 1, 5], 30, [[2, 5], [9, 5], [10, 5], [11, 5]])
