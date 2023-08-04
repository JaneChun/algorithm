const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
const lines = fs.readFileSync(filePath).toString().trim().split('\n');

const n = parseInt(lines[0]);
const candies = [];
let maxConnection = 0;

for (let i = 1; i <= n; i++) {
	const arr = lines[i].split('');
	candies.push(arr);
}

for (let i = 0; i < n; i++) {
	for (let j = 0; j < n - 1; j++) {
		[candies[i][j], candies[i][j + 1]] = [candies[i][j + 1], candies[i][j]];
		const count = checkConnection(candies, 'row');
		maxConnection = Math.max(maxConnection, count);
		[candies[i][j], candies[i][j + 1]] = [candies[i][j + 1], candies[i][j]]; // 원상복귀
	}
}

for (let i = 0; i < n - 1; i++) {
	for (let j = 0; j < n; j++) {
		[candies[i][j], candies[i + 1][j]] = [candies[i + 1][j], candies[i][j]];
		const count = checkConnection(candies, 'column');
		maxConnection = Math.max(maxConnection, count);
		[candies[i][j], candies[i + 1][j]] = [candies[i + 1][j], candies[i][j]]; // 원상복귀
	}
}

function checkConnection(arr, direction) {
	let maxCount = 1;

	for (let i = 0; i < n; i++) {
		let count = 1;
		for (let j = 0; j < n - 1; j++) {
			if (arr[i][j] === arr[i][j + 1]) {
				count++;
				maxCount = Math.max(maxCount, count);
			} else {
				count = 1;
			}
		}
	}

	for (let i = 0; i < n; i++) {
		let count = 1;
		for (let j = 0; j < n - 1; j++) {
			if (arr[j][i] === arr[j + 1][i]) {
				count++;
				maxCount = Math.max(maxCount, count);
			} else {
				count = 1;
			}
		}
	}

	return maxCount;
}

console.log(maxConnection);
