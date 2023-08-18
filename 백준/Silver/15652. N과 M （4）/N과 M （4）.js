const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
const input = fs.readFileSync(filePath).toString().trim().split(' ').map(Number);

const [N, M] = input;
let answer = [];

const dfs = (arr, num) => {
	if (arr.length === M) {
		answer.push([...arr]);
		return;
	}

	for (let i = num; i <= N; i++) {
		arr.push(i);
		dfs(arr, i);
		arr.pop();
	}
};

for (let i = 1; i <= N; i++) {
	dfs([i], i);
}

answer = answer.map((arr) => arr.join(' ')).join('\n');

console.log(answer);
