const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : './input_6064.txt';
const lines = fs.readFileSync(filePath).toString().trim().split('\n');

const T = Number(lines[0]);
const tests = lines.slice(1).map((line) => line.split(' ').map((e) => Number(e)));
const answer = [];

function gcd(x, y) {
	let a = Math.max(x, y);
	let b = Math.min(x, y);
	let r;
	while (true) {
		r = a % b;
		if (r === 0) return b;
		a = b;
		b = r;
	}
}

for (const test of tests) {
	const [M, N, x, y] = test;
	let year = -1;

	const lcm = (M * N) / gcd(M, N);

	for (let i = x; i <= lcm; i += M) {
		if ((i - 1) % N + 1 === y) {
			year = i;
		}
	}
	answer.push(year);
}

console.log(answer.join('\n'));
