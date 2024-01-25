function solution(weights) {
    var answer = 0;
    const cal = [ 1/2, 1/1, 2/3, 3/4 ] // 경우의 수
    const memo = {}
    
    weights.sort((a, b) => a - b).forEach((weight) => {
        for (let i of cal) {
            const now = weight  * i
            if (memo[now]) answer += memo[now]
        }
        
        if (memo[weight]) memo[weight]++
        else memo[weight] = 1
    })
    return answer
}