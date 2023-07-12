function solution(n, computers) {
    let count = 0;
    const visited = Array.from({length: n}, () => false);
    
    const dfs = (node) => {
        visited[node] = true;
        const connectionArr = computers[node];

        for (let i = 0; i < connectionArr.length; i++) {
            if (connectionArr[i] === 1 && !visited[i]) {
                dfs(i);
            }
        }
    }
    
    for (let node = 0; node < computers.length; node++) {
        if (!visited[node]) { 
            dfs(node);
            count++;
        }
    }
    
    return count;
}