function solution(d, budget) {
    let count = 0;
    d.sort((a, b) => a - b); // [1,2,3,4,5]
    for (let i = 0; i < d.length; i++) {
        budget -= d[i]; // 9 - 1 = 8
        count++; // 1
        if (budget === 0) {
            break;
        } else if (budget < 0) {
            return count - 1;
        } 
    }
    return count;
}