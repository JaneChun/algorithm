function solution(s) {
    let count = 0;
    const n = s.length;
    const pair = {'(' : ')', '{' : '}', '[' : ']'};

    for (let i  = 1; i <= n; i++) {
        const stack = [];
        
        if (!pair[s[0]]) { // 첫번째부터 닫는 괄호라면 얼리 리턴
            console.log('얼리 리턴', pair[s[0]])
            s = s.substr(1) + s[0];
            continue;
        }; 
        
        for (const bracket of s) {
            if (pair[bracket]) { // 여는 괄호면 스택에 넣고,
                stack.push(bracket);
                continue;
            }
            
            const top = stack[stack.length - 1]
            if (pair[top] === bracket) { // 닫는 괄호면, 스택의 맨 위 요소와 짝이 맞는다면
                stack.pop(); // pop해준다.
                continue;
            }
        }
        
        if (stack.length === 0) count++; // 올바른 괄호라면 카운트 + 1
        s = s.substr(1) + s[0];
    }
    
    return count;
}