function solution(n) {
    const count = n.toString(2).split('').filter((digit) => digit === '1').length;
    
    while (true) {
        n++;
        const nextCount = n.toString(2).split('').filter((digit) => digit === '1').length;
        
        if (count === nextCount) return n;
    }
}
