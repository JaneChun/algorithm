function solution(n, times) {
    const sortedTimes = times.sort((a, b) => a - b);
    let left = 1;
    let right = sortedTimes.at(-1) * n;
    
    while (left <= right) {
        const mid = Math.floor((left + right) / 2);
        const sum = sortedTimes.reduce((acc, time) => acc + Math.floor(mid / time) , 0)
        
        if (sum < n) {
            left = mid + 1
        } else {
            right = mid - 1
        }
    }
    
    return left;
}