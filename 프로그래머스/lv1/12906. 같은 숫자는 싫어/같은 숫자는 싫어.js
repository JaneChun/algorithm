function solution(arr) {
    const result = [];
    arr.forEach((v) => result[result.length - 1] !== v ? result.push(v) : v);
    return result;
}