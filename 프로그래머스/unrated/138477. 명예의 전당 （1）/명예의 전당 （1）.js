function solution(k, score) {
    const hallOfFame = [];
    const lowestArr = [];
    let lowest = 0;
    
    for (let i = 0; i < score.length; i++) {
        if (i < k) { // i가 k번째보다 작을 경우
            hallOfFame.push(score[i]); // 명예의 전당에 넣기
            hallOfFame.sort((a, b) => a - b); // 정렬
            lowest = hallOfFame[0] // 최저값 0번째
            lowestArr.push(lowest); // 
        } else { // i > k번째
            if (score[i] > lowest) {
                hallOfFame.shift(); // k번째 방출
                hallOfFame.push(score[i]); // score[i] 넣기
                hallOfFame.sort((a, b) => a - b); // 정렬
            }
            lowest = hallOfFame[0] // 최저값 0번째
            lowestArr.push(lowest); //
        }
    }
    
    return lowestArr;
}