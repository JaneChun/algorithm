function solution(citations) {
    let hIndex = 0;
    citations.sort((a, b) => b - a);
    for (let i = 0; i < citations.length; i++) {
        if (citations[i] >= i + 1) {
            hIndex = i + 1;
            console.log(citations[i], '>=', i, '=', citations[i] >= i)
        }
    }
    return hIndex;
}
