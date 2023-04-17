function solution(n, m, section) {
    let count = 1;
    let cur = section[0];
    
    for (const sec of section) {
        if (cur + m - 1 < sec) {
            cur = sec;
            count++;
        }
    }
    
    return count;
}
