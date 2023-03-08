// function solution(arr) {
//     const result = [];
//     arr.forEach((v) => result[result.length - 1] !== v ? result.push(v) : v);
//     return result;
// }

function solution(arr) {
    return arr.filter((v, i) => v !== arr[i - 1]);
}