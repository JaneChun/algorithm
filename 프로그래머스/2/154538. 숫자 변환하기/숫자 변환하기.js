function solution(x, y, n) {
    const dp = Array(y + 1).fill(Infinity)
    dp[x] = 0 // x에서 i를 만들 수 있는 최소 연산횟수를 dp[i]에 저장
    // x부터 y까지 돌면서 dp[i]를 업데이트한다.
    
    for (let i = x; i <= y; i++) {
        dp[i + n] = Math.min(dp[i + n], dp[i] + 1)
        dp[i * 2] = Math.min(dp[i * 2], dp[i] + 1)
        dp[i * 3] = Math.min(dp[i * 3], dp[i] + 1)
    }
    
    return dp[y] === Infinity ? -1 : dp[y]
}

// DFS 풀이 (시간초과)
// function solution(x, y, n) {
//     let min = Infinity
//     const dfs = (x, count) => {
//         if (x === y) return min = Math.min(min, count)
//         if (x > y) return
//         dfs(x + n, count + 1)
//         dfs(x * 2, count + 1)
//         dfs(x * 3, count + 1)
//     }
//     dfs(x, 0)
    
//     return min === Infinity ? -1 : min
// }