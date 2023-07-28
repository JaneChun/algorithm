function solution(n, edge) {
    const graph = Array.from(Array(n + 1), () => []);
    
    edge.forEach(([a, b]) => {
        graph[a].push(b);
        graph[b].push(a);
    });
    
    const distance =  Array(n + 1).fill(0);
    distance[1] = 1;
    
    const queue = [];
    queue.push(1);
    while (queue.length) {
        const from = queue.shift();
        for (const dest  of graph[from]) {
            if (distance[dest] === 0) {
                queue.push(dest);
                distance[dest] = distance[from] + 1;
            }
        }
    }
    
    const max = Math.max(...distance);
    return distance.filter((d) => d === max).length;
}