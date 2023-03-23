function solution(a, b, n) {
    let received = 0;
    while (n >= a) {
        let give = Math.floor(n / a);
        n -= a * give;
        n += give * b;
        received += give * b;
    }
    return received;
}