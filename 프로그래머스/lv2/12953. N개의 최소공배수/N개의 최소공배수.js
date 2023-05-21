function solution(arr) {
    while(arr.length > 1) {
        const a = arr.pop();
        const b = arr.pop();
        const lcm = a * b / gcd(a, b);
        arr.push(lcm);
    }
    return arr[0];
}

function gcd(a, b) {
    if (b === 0) {
        return a;
    }
    return gcd(b, a % b);
}