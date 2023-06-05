function solution(k, tangerine) {
    let result = 0;
    const map = new Map();
    
    tangerine.forEach((t) => {
        if (map.has(t)) map.set(t, map.get(t) + 1);
        else map.set(t, 1);
    })
    
    const sortedArr = [...map].sort((a, b) => b[1] - a[1]);
    console.log(sortedArr)
    
    for (const [size, quantity] of sortedArr) {
        if (k <= 0) break; // 0
        k -= quantity; // 0
        result++; // 상자 1개에 3종류
    }
    
    return result;
}