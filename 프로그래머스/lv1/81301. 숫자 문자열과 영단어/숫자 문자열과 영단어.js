function solution(s) {
    const numbers = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'];
    numbers.forEach((v, i) => {
        const regex = new RegExp(`${numbers[i]}`, 'g');
        s = s.replace(regex, i);
    })
    return Number(s);
}