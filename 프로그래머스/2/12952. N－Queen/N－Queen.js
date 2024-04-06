function possible(x, y, queens) {
    for (const [a, b] of queens) {
        if (a === x || b === y) return false // 어느 하나의 퀸과 x열이나 y열이 같으면 안됨 
        if (Math.abs(a - x) === Math.abs(b - y)) return false // 어느 하나의 퀸과 같은 대각선상에 있으면 안됨
    }
    return true
}

function placeQueens(n, row, queens,count) {
    if (row === n) { // base case : 모든 퀸을 배치한 경우
        return count + 1
    }
    
    for (let col = 0; col < n; col++) {
        if (possible(row, col, queens)) {
            queens.push([row, col]) // 퀸 배치
            count = placeQueens(n, row + 1, queens, count) // 다음 행에 퀸 배치
            queens.pop(); // 퀸 제거 (백트래킹)
        }
    }
    return count
}

function solution(n) {
    let count = 0
    count = placeQueens(n, 0, [], count)
    return count
}