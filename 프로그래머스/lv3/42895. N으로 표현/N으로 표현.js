function solution(N, number) {
     const dpTable = Array.from({ length : 9 }, () => new Set());
    
    dpTable.forEach((set, i) => {
        if (i !== 0) set.add(Number(String(N).repeat(i))); 
    })
    
    for (let n = 1; n <= 8; n++) {
        for (let i = 1; i <= n - 1; i++) {
            for (const a of dpTable[i]) {       
                for (const b of dpTable[n - i]) {
                    dpTable[n].add(a + b);
                    dpTable[n].add(a - b);
                    dpTable[n].add(a * b);
                    dpTable[n].add(Math.floor(a / b));
                }
            }
        }
        if (dpTable[n].has(number)) return n;
    }
    return -1;
}