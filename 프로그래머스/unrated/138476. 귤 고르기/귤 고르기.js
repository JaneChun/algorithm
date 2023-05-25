function solution(k, tangerine) {
    let result = 0;
    const map = new Map();
    
    tangerine.forEach((t) => {
        if (map.has(t)) map.set(t, map.get(t) + 1);
        else map.set(t, 1);
    })
    
    const sortedArr = [...map].sort((a, b) => b[1] - a[1]);
    
    for (const [size, quantity] of sortedArr) {
        if (k <= 0) break;
        k -= quantity;
        result++;
    }
    
    return result;
}