function timeToMin(time) {
  const [hh, mm] = time.split(':').map(Number);
  return hh * 60 + mm;
}

function solution(plans) {
    const result = []
    const stack = []
        
    const sortedPlans = plans.map(([name, start, playtime]) => ({name, start: timeToMin(start), playtime: Number(playtime)}))
                 .sort((a, b) => a.start - b.start)
    
    for (let i = 0; i < sortedPlans.length - 1; i++) {
        const {name, start, playtime} = sortedPlans[i]
        const {start: nextStart} = sortedPlans[i + 1]
        const end = start + playtime
        // 1. 다음 과목 시작 전에 끝낸 경우
        if (end <= nextStart) {
            result.push(name)
            let freetime = nextStart - end // 남은 시간 계산
            
            // 남은 시간 동안 멈춰둔 과제 수행
            while (stack.length) {
                const {name: stName, playtime: stPlaytime} = stack.pop()
                if (stPlaytime <= freetime) { // 1-1. 남은 시간 안에 끝낸 경우
                    freetime -= stPlaytime
                    result.push(stName)
                } else { // 1-2. 남은 시간 안에 못 끝낸 경우
                    stack.push({name: stName, playtime: stPlaytime - freetime})
                    break
                }
            }
        } else {
            // 2. 다음 과목 시작 전에 못끝낸 경우
            stack.push({name, playtime: playtime - (nextStart - start)})
        }
    }
    
    result.push(sortedPlans[sortedPlans.length - 1].name) // 마지막 과제 완료 처리
    
    while (stack.length) {
        result.push(stack.pop().name) // 멈춰둔 과제 순서대로 완료 처리
    }
            
    return result
}