const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
const input = fs
	.readFileSync(filePath)
	.toString()
	.trim()
	.split('\n')
	.map((str) => parseInt(str));

function solution(input) {
	const dwarfArr = input;
	const sumOfNine = dwarfArr.reduce((acc, cur) => acc + cur, 0);
	let answer;

	for (let i = 0; i < sumOfNine - 1; i++) {
		for (let j = i + 1; j < sumOfNine; j++) {
			if (sumOfNine - dwarfArr[i] - dwarfArr[j] === 100) {
				answer = dwarfArr.filter((height) => height !== dwarfArr[i] && height !== dwarfArr[j]);
			}
		}
	}
	return answer.sort((a, b) => a - b).join('\n');
}

console.log(solution(input));
