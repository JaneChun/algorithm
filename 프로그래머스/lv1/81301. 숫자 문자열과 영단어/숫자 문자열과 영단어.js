function solution(s) {
    const numbers = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'];
    numbers.forEach((v, i) => {
        let arr = s.split(numbers[i]);
        s = arr.join(i);
    })
    return Number(s);
}