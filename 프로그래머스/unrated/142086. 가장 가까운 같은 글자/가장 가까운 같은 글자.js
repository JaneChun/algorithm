function solution(s) {
    const result = [];
    const memo = [];
    for (let i = 0; i < s.length; i++) {
        if (!memo.includes(s[i])) {
            memo.push(s[i]);
            result.push(-1);
        } else {
            const idx = s.slice(0, i).lastIndexOf(s[i]);
            result.push((i - idx));
        }
    }
    return result;
}