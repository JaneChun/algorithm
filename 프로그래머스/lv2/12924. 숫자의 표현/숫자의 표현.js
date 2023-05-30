function solution(n) {
    let result = 0;
    for (let i = 1; i <= n; i++) {
        let sum = i;
        for(let j = i + 1; j <= n; j++) {
            sum += j;
            if (sum === n) {
                result++;
                break;
            } else if (sum > n) {
                break;
            }
        }
    }
    return result;
}