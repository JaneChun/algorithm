function solution(n) {
    const sieve = new Array(n + 1).fill(true);
    
    for (let i = 2; i <= n; i++) {
        if (sieve[i] === false) continue;  // 이미 지워진 숫자라면 무시
        
        // 이미 지워진 숫자가 아니라면
        for (let j = i + i; j <= n; j += i) { // 본인 제외 배수부터 시작해서 다 지워준다.
            sieve[j] = false;
        }
    }
    
    return sieve.filter((el) => el).length - 2;
}