function solution(d, budget) {
    let count = 0;
    d.sort((a, b) => a - b);
    for (let i = 0; i < d.length; i++) {
        budget -= d[i];
        count++;
        if (budget === 0) {
            return count;
        } else if (budget < 0) {
            return count - 1;
        } 
    }
    return count;
}