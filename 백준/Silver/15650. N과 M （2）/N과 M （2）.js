const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
const input = fs.readFileSync(filePath).toString().trim().split(' ').map(Number);

const [N, M] = input;

const answer = [];

const dfs = (num, arr, used) => {
	if (arr.length === M) {
		return answer.push([...arr]);
	}

	if (arr.length > M) return;

	for (let i = num; i <= N; i++) {
		if (!used[i]) {
			arr.push(i);
			used[i] = true;
			dfs(i, arr, used);
			used[i] = false;
			arr.pop();
		}
	}
};

for (let i = 1; i <= N; i++) {
	const used = new Array(N + 1).fill(false);
	used[i] = true;
	dfs(i, [i], used);
}

console.log(answer.map((arr) => arr.join(' ')).join('\n'));
