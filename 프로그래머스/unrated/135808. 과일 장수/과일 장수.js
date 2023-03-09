function solution(k, m, score) {
    let result = 0;
    sorted = score.sort((a, b) => b - a);
    for(let i = m - 1; i < score.length; i += m) {
        result += score[i] * m;
    }
    return result;
}