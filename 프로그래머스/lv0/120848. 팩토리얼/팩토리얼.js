function solution(n) {
    let acc = 1;
    
    for (let i = 1; i <= n; i++) {
        acc = acc * i;
        if (acc === n) return i;
        else if (acc > n) return i - 1;
    }
    
}