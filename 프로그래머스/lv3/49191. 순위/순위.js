function solution(n, results) {
    const graph = Array.from({length : n}, (_, i) => Array.from({length : n}, (_, j) => i === j ? 0 : false));
    
    results.forEach(([winner, loser]) => {
        graph[winner - 1][loser - 1] = 1;
        graph[loser - 1][winner - 1] = -1;
    });
    
    for (let mid = 0; mid < n; mid++) {
        for (let a = 0; a < n; a++) {
            for (let b = 0; b < n; b++) {
                // a가 mid를 이기고, mid가 b를 이기면 a가 b를 이김
                if (graph[a][mid] === 1 && graph[mid][b] === 1) {
                    graph[a][b] = 1;
                }
                // a가 mid에게 지고, mid가 b에게 지면 a가 b에게 짐
                if (graph[a][mid] === -1 && graph[mid][b] === -1) {
                    graph[a][b] = -1;
                }
            }
        }
    }
    
    
    let answer = 0;
    graph.forEach((player) => {
        if (player.includes(false)) return;
        answer++;
    });
    
    return answer;
}