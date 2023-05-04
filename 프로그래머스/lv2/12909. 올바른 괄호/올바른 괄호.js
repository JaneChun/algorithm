function solution(s){
    let count = 0;
    for (let i = 0; i < s.length; i++) {
        if (count === -1) return false;
        if (s[i] === '(') {
            count += 1;
        } else {
            count -=1;
        }
    }
    
    return count === 0 ? true : false;
}