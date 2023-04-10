function solution(lottos, win_nums) {
    let zeroCount = 0; // 0의 개수
    let winCount = 0; // 맞춘 번호 개수
    const ranks = {0: 6, 1: 6, 2: 5, 3: 4, 4: 3, 5: 2, 6: 1}
    
    for (let i = 0; i < lottos.length; i++) {
        if (lottos[i] === 0) zeroCount++;
        else {
            win_nums.filter((num) => num === lottos[i]).length > 0 && winCount++;
        }
    }
    return [ranks[winCount + zeroCount], ranks[winCount]];
} // 최저 등수 : winCount / 최고 등수 : zero + win
