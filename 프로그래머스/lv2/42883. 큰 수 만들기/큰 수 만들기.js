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
    
    while (count < k) { // 지운 숫가 개수 < k
        stack.pop(); // 뒤에서부터 삭제
        count++;
    }
    
    return stack.join('');
}