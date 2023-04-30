function solution(ingredient) {
    let count = 0;
    const stack = [];
    
    ingredient.forEach((item) => {
        stack.push(item);
        
        if (stack.length < 4) return;
        if (stack[stack.length - 1] !== 1) return;
        if (stack[stack.length - 2] !== 3) return;
        if (stack[stack.length - 3] !== 2) return;
        if (stack[stack.length - 4] !== 1) return;
        
        for (let i = 1; i <= 4; i++) {
            stack.pop();
        }
        count++;
    })
    return count;
}