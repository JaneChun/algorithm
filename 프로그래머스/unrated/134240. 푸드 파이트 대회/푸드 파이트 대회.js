function solution(food) {
    const front = food.map((v) => Math.floor(v / 2))
        .reduce((acc, cur, i) => acc + `${i}`.repeat(cur), '');
    const back = front.split('').reverse().join('')
    return front + '0' + back;
}