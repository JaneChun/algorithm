function solution(n) {
    return '수박'.repeat(n/2).concat(n % 2 === 1 ? '수' : '');
}