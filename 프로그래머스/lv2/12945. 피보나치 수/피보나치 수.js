function solution(n) {
    let memo = [0, 1];

    function fibo(n) {
        for(let i = 2; i <= n; i++) {
            memo[i] = (memo[i - 1] + memo[i - 2]) % 1234567;
        }
    
        return memo[n];
    }
    
    return fibo(n);
}