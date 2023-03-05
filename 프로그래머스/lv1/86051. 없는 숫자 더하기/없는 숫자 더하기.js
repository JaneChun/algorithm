function solution(numbers) {
    let result = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0];
    numbers.forEach((num) => result.includes(num) ? result.splice(result.indexOf(num), 1) : result)
    return result.reduce((acc, cur) => acc + cur);
}