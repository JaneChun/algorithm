const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
const lines = fs.readFileSync(filePath).toString().trim().split('\n');

const numOfCity = parseInt(lines[0]);
const numOfBus = parseInt(lines[1]);
const busCostTable = [];

for (let i = 2; i < lines.length; i++) {
	const [from, to, cost] = lines[i].split(' ').map(Number);
	busCostTable.push([from, to, cost]);
}

const graph = Array.from({ length: numOfCity }, (_, i) => Array.from({ length: numOfCity }, (_, j) => (i === j ? 0 : Infinity)));

for (const [from, to, cost] of busCostTable) {
	graph[from - 1][to - 1] = Math.min(graph[from - 1][to - 1], cost);
}

for (let mid = 0; mid < numOfCity; mid++) {
	for (let from = 0; from < numOfCity; from++) {
		for (let to = 0; to < numOfCity; to++) {
			if (graph[from][mid] + graph[mid][to] < graph[from][to]) {
				graph[from][to] = graph[from][mid] + graph[mid][to];
			}
		}
	}
}

for (let i = 0; i < numOfCity; i++) {
	for (let j = 0; j < numOfCity; j++) {
		if (graph[i][j] === Infinity) graph[i][j] = 0;
	}
}

graph.forEach((arr) => {
	console.log(arr.join(' '));
});
