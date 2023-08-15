const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
const input = fs.readFileSync(filePath).toString().trim().split(' ').map(Number);

const [N, M] = input;

const answer = [];

const dfs = (arr) => {
	if (arr.length === M) {
		return answer.push([...arr]);
	}

	if (arr.length > M) return;

	for (let i = 1; i <= N; i++) {
		arr.push(i);
		dfs(arr);
		arr.pop();
	}
};

for (let i = 1; i <= N; i++) {
	dfs([i]);
}

console.log(answer.map((arr) => arr.join(' ')).join('\n'));
