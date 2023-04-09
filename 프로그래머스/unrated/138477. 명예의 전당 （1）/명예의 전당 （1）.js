function solution(k, score) {
    const hallOfFame = [];
    const lowestArr = [];
    let lowest = 0;
    
    for (let i = 0; i < score.length; i++) {
        if (i < k) {
            hallOfFame.push(score[i]);
            hallOfFame.sort((a, b) => a - b);
            lowest = hallOfFame[0]
            lowestArr.push(lowest);
        } else {
            if (score[i] > lowest) {
                hallOfFame.shift();
                hallOfFame.push(score[i]);
                hallOfFame.sort((a, b) => a - b);
            }
            lowest = hallOfFame[0]
            lowestArr.push(lowest);
        }
    }
    
    return lowestArr;
}