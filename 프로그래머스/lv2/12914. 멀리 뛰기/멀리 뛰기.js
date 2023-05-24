function solution(n) {
    const table = [1n, 1n, 2n];
    
    for (let i = 3; i <= n; i++) {
        table.push(table[i - 1] + table[i - 2]);
    }
    
    return table[n] % 1234567n;
}
