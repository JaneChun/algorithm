function solution(keymap, targets) {
    const hash = {};
    keymap.forEach((keys) => { // keys = 'ABACD'
        [...keys].forEach((key, i) => { // key = 'A' // i = 눌러야 하는 횟수
            hash[key] ? hash[key] = Math.min(hash[key], i + 1) : hash[key] = i + 1;
        }) // hash에 이미 값이 있으면 기존 값과 현재 값을 비교해 최소값 저장, 없으면 현재 값 추가
    })
    // hash = { A: 1, B: 1, C: 2, D: 5, E: 3, F: 4 } -> 최소 횟수만 저장된다.
    
    const answer = [];
    
    for (const target of targets) { // target = 'ABCD'
        let count = 0;
        
        for (const key of target) { // key = 'A'
           count += hash[key];
           console.log(hash[key])
        }
        answer.push(count || -1);
    }
    return answer;
}