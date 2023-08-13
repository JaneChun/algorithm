const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
const input = fs.readFileSync(filePath).toString().trim().split('\n').map(Number);

const arr = input.slice(1);
const answer = [];

for (const N of arr) {
	let count = 0;
	const dfs = (target, sum) => {
		if (sum === target) return count++;
        if (sum > target) return;
        dfs(target, sum + 1);
        dfs(target, sum + 2);
        dfs(target, sum + 3);
	};

	dfs(N, 0);

	answer.push(count);
}

console.log(answer.join('\n'));