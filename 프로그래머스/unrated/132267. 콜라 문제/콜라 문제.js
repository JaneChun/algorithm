function solution(a, b, n) {
    let received = 0;
    while (n >= a) {
        let give = Math.floor(n / a); // 10묶음
        n -= a * give; // 20 - 10 * 2 = 0
        n += give * b; // 0 + 10 * 1 = 10
        received += give * b; // 10
    }
    return received;
}