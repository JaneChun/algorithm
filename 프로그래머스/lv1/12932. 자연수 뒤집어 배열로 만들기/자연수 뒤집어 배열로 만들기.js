function solution(n) {
    return String(n).split('').map((el) => parseInt(el)).reverse();
}