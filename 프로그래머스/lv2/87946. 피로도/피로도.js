function solution(k, dungeons) {
    let max = 0;
    const visited = Array.from({length: dungeons.length}, () => false); // [ false, false, false ]
    
    function dfs(hp, completed) {
        for (let i = 0; i < dungeons.length; i++) { // 0
            const [need, consume] = dungeons[i]; // [80, 20]
            if (!visited[i] && hp >= need) {
                visited[i] = true;
                dfs(hp - consume, completed + 1); // dfs(60, 1) -> dfs(20, 2)
                visited[i] = false;
            }
        }
        
        max = Math.max(max, completed); // 최대 던전 클리어횟수 업데이트
    }
    
    dfs(k, 0); // dfs(80, 0)
    
    return max;
}

//        [80, 20]                [50, 40]                [30, 10]
//  [50, 40]    [30, 10]    [80, 20]    [30, 10]     [80, 20]    [50, 40] 
//  [30, 10]    [50, 40]    [30, 10]    [80, 20]     [50, 40]    [80, 20] 