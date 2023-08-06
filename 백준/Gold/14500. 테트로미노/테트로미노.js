const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : './input_14500.txt';
const lines = fs.readFileSync(filePath).toString().trim().split('\n');

const [N, M] = lines[0].split(' ').map(Number);
const board = lines.slice(1).map((line) => line.split(' ').map(Number));

const shapes = [
	[
		[1, 1],
		[1, 1],
	], // 네모

	[[1, 1, 1, 1]], // 길쭉이 1
	[[1], [1], [1], [1]], // 길쭉이 2

	[
		[1, 1, 1],
		[0, 1, 0],
	], // T-모양 1
	[
		[0, 1, 0],
		[1, 1, 1],
	], // T-모양 2
	[
		[1, 0],
		[1, 1],
		[1, 0],
	], // T-모양 3
	[
		[0, 1],
		[1, 1],
		[0, 1],
	], // T-모양 4

	[
		[1, 1, 0],
		[0, 1, 1],
	], // 꺾은 모양 1
	[
		[0, 1, 1],
		[1, 1, 0],
	], // 꺾은 모양 2
	[
		[1, 0],
		[1, 1],
		[0, 1],
	], // 꺾은 모양 3
	[
		[0, 1],
		[1, 1],
		[1, 0],
	], // 꺾은 모양 4

	[
		[1, 1, 1],
		[0, 0, 1],
	], // L-모양 1
	[
		[0, 0, 1],
		[1, 1, 1],
	], // L-모양 2
	[
		[1, 1, 1],
		[1, 0, 0],
	], // L-모양 3
	[
		[1, 0, 0],
		[1, 1, 1],
	], // L-모양 4

	[
		[1, 1],
		[1, 0],
		[1, 0],
	], // L-모양 5
	[
		[1, 1],
		[0, 1],
		[0, 1],
	], // L-모양 6
	[
		[1, 0],
		[1, 0],
		[1, 1],
	], // L-모양 7
	[
		[0, 1],
		[0, 1],
		[1, 1],
	], // L-모양 8
];

let max = 0;
for (const shape of shapes) {
	const height = shape.length;
	const width = shape[0].length;

	for (let i = 0; i <= N - height; i++) {
		for (let j = 0; j <= M - width; j++) {
			let value = 0;
			for (let h = 0; h < height; h++) {
				for (let w = 0; w < width; w++) {
					value += shape[h][w] * board[i + h][j + w];
				}
			}
			max = Math.max(max, value);
		}
	}
}
console.log(max);
