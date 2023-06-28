function solution(k, dungeons) {
    let count = 0;
    const visited = Array.from({length: dungeons.length}, () => false);
    
    function dfs(hp, depth) {
        if (count < depth) count = depth;
        
        for (let i = 0; i < dungeons.length; i++) {
            const [need, consume] = dungeons[i];
            if (!visited[i] && hp >= need) {
                visited[i] = true;
                dfs(hp - consume, depth + 1);
                visited[i] = false;
            }
        }
    }
    
    dfs(k, 0);
    
    return count;
}