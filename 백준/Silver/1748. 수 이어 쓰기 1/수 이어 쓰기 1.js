const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
const input = fs.readFileSync(filePath).toString();

const N = Number(input);
let answer = 0;

for (let i = 1; i <= N; i *= 10) {
	answer += N - i + 1;
}

console.log(answer);