function solution(wallpaper) {
    const rowLen = wallpaper.length, colLen = wallpaper[0].length;
    const matrix = Array.from(wallpaper, (row) => Array.from(row, (char) => char === '.' ? 0 : 1))
    // [ 
    //   [ 0, 1, 0, 0, 0 ], 
    //   [ 0, 0, 1, 0, 0 ], 
    //   [ 0, 0, 0, 1, 0 ] 
    //]
    
// [
//   [0, 0, 0, 0, 0,0, 0, 0, 0, 0],
//   [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
//   [0, 0, 0, 0, 0, 0, 1, 1, 0, 0],
//   [0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
//   [0, 0, 0, 0, 1, 0, 0, 0, 0, 0]
// ]
    
    // 가장 max 왼쪽 값, max 위쪽 값, max 오른쪽 값, max 아래 값을 찾아야 한다. => S(위, 왼), E(아래, 오)
    let left = colLen - 1, up = rowLen - 1, right = 0, down = 0;
    for (let row = 0; row < rowLen; row++) {
        for (col = 0; col < colLen; col++) {
            const value = matrix[row][col]
            if (value) {
                console.log('row, col', row, col)
                up = Math.min(up, row)
                left = Math.min(left, col)
                down = Math.max(down, row + 1)
                right = Math.max(right, col + 1) // 최대값이 바탕화면을 넘어갈 때는 + 1 하지 않는다.
                console.log('[위, 왼, 아래, 오]', [up, left, down, right])
            }
        }
    }
    return [up, left, down, right]
}