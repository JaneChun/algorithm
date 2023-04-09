function solution(number, limit, power) {
    return Array.from(new Array(number), (v, i) => i + 1).reduce((acc, num) => {
        let divisorsCount = 0;
        const square = Math.sqrt(num);
        for (let i = 1; i <= Math.floor(square); i++) {
            if (num % i === 0) divisorsCount++;
        }
        const attack = Number.isInteger(square) ? divisorsCount * 2 - 1 : divisorsCount * 2;
        return attack > limit ? acc + power : acc + attack;
    }, 0)
}