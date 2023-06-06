function solution(n, left, right) {
    const result = [];
    
    while(left <= right) {
        result.push(Math.max(Math.floor(left / n), left % n) + 1); 
        left++;
    }
    
    return result;
}