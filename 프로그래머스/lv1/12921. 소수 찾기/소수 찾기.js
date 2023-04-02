function solution(n) {
    let count = 0;
    for (let i = 2; i <= n; i++) {
        if (isPrimeNumber(i)) count++;
    }
    return count;
}
// 3
function isPrimeNumber(num) {
    if (num === 1) return false;
    if (num === 2) return true;
    if (num % 2 === 0) return false; 
    for(let i = 3; i <= Math.sqrt(num); i+=2) {
        if (num % i === 0) return false;
    }
    
    return true;
}