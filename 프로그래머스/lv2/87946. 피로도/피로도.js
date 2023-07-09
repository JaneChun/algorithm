function solution(k, dungeons) {
    let max = 0;
    const visited = Array.from({length: dungeons.length}, () => false);
    
    function dfs(hp, completed) {
        for (let i = 0; i < dungeons.length; i++) {
            const [need, consume] = dungeons[i];
            if (!visited[i] && hp >= need) {
                visited[i] = true;
                dfs(hp - consume, completed + 1);
                visited[i] = false;
            }
        }
        
        max = Math.max(max, completed); // 최대 던전 클리어횟수 업데이트
    }
    
    dfs(k, 0);
    
    return max;
}

//        [80, 20]                [50, 40]                [30, 10]
//  [50, 40]    [30, 10]    [80, 20]    [30, 10]     [80, 20]    [50, 40] 
//  [30, 10]    [50, 40]    [30, 10]    [80, 20]     [50, 40]    [80, 20] 