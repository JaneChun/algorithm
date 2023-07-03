function solution(n, wires) {
    let minDiff = 99;
    const tree = Array.from({length: n + 1}, () => []);
    
    wires.forEach(([v1, v2]) => {
        tree[v1].push(v2);
        tree[v2].push(v1);
    });

    const bfs = (tree, root, exceptNode) => {
        const visited = new Array(tree.length).fill(false);
        const queue = [root];
        let count = 0;
        
        while (queue.length) {
            const src = queue.shift();
            visited[src] = true;
             
            for (const dest of tree[src]) {
                if (dest !== exceptNode && visited[dest] === false) {
                    queue.push(dest);
                }
            }
            count++;
        }
        
        return count;
    }
    
    for (const [v1, v2] of wires) {
        minDiff = Math.min(minDiff, Math.abs(bfs(tree, v1, v2) - bfs(tree, v2, v1)));
    }

    return minDiff;
}