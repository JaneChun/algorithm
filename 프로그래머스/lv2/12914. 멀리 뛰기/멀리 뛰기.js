function solution(n) {
    const table = [1, 1];
    
    for (let i = 2; i <= n; i++) {
        table.push((table[i - 1] + table[i - 2]) % 1234567);
    }
    
    return table[n];
}