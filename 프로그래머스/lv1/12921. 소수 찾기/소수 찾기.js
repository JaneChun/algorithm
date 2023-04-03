function solution(n) {
    const sieve = [];
    
    for (let k = 2; k <= n; k++) {
        sieve[k] = k;
    }
    
    for (let i = 2; i <= n; i++) {
        if (sieve[i] === false) continue;
        
        for (let j = i + i; j <= n; j += i) {
            sieve[j] = false;
        }
    }
    
    return sieve.filter((el) => el).length;
}