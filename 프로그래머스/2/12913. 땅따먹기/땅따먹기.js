function solution(land) {
    for (let i = 1; i < land.length; i++) {
        for (let j = 0; j < 4; j++) {
            // 같은 인덱스는 제외한 이전 land 배열
            const prevLand = land[i - 1].filter((_, _i) => j !== _i)
            land[i][j] += Math.max(...prevLand)
        }
    }
    console.log(land)
    return Math.max(...land.pop())
}