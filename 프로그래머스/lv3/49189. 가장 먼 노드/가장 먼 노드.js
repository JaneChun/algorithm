function solution(n, edge) {
    const graph = Array.from(Array(n + 1), () => []);
    
    edge.forEach(([a, b]) => {
        graph[a].push(b);
        graph[b].push(a);
    });
    
    const distance = Array(n + 1).fill(0); // [0, 1, 2, 2, 0, 0, 0]
    distance[1] = 1;
    
    const queue = [];
    queue.push(1); // queue = [4 6 5]
    while (queue.length) {
        const from = queue.shift(); // from = 1
        for (const dest  of graph[from]) { // graph[1] = [3, 2] // dest = 3, dest = 2
            if (distance[dest] === 0) { // 방문 X
                queue.push(dest); // [3]
                distance[dest] = distance[from] + 1;
            }
        }
    }
    const max = Math.max(...distance);
    return distance.filter((d) => d === max).length;
}
  // graph
  //   	[
  // [],
  // [ 3, 2 ],
  // [ 3, 1, 4, 5 ],
  // [ 6, 4, 2, 1 ],
  // [ 3, 2 ],
  // [ 2 ],
  // [ 3 ],
  // []
  //   ]