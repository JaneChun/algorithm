function solution(n) {
    return String(n).split('').reduce((acc, cur) => Number(acc) + Number(cur), 0);
}