function solution(n, m) {
    let GCD;
    for(let i = 1; i <= n; i++) {
        if (n % i === 0 && m % i === 0) {
            GCD = i;
        }
    }
        
    let LCM = GCD * (n / GCD) * (m / GCD);
    return [GCD, LCM];
}