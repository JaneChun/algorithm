const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
const input = fs.readFileSync(filePath).toString().trim().split(' ').map(Number);

const [N, M] = input;
let answer = [];

const dfs = (arr, visited) => {
	if (arr.length === M) {
		return answer.push([...arr]);
	}

	for (let i = 1; i <= N; i++) {
		if (!visited[i]) {
			arr.push(i);
			visited[i] = true;
			dfs(arr, visited);
			visited[i] = false;
			arr.pop();
		}
	}
};
const visited = Array(N + 1).fill(false);
dfs([], visited);

answer = answer.map((arr) => arr.join(' ')).join('\n');

console.log(answer);