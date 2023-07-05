function solution(number, k) {
    let count = 0;
    const stack = [];
    
    for (const n of number) {
        while (stack && stack[stack.length - 1] < n && count < k) {
            stack.pop();
            count++;
        }
        
        stack.push(n);        
    }
    
    while (count < k) {
        stack.pop();
        count++;
    }
    
    return stack.join('');
}