function solution(s) { // "for the last week"
    const arr = s.split(' '); // ["for", "the", "last", "week"]
    let result = [];
    
    
    for(let el of arr) { // el = "for"    
    let str = '';
        for(let i = 0; i < el.length; i++) {
            if (i === 0 && typeof el[i] === 'string') {
                str = str + el[i].toUpperCase();
            } else {
                str = str + el[i].toLowerCase();
            }
        } // inner 반복문 끝
        result.push(str);
    } // outer 반복문 끝
    return result.join(' ');
}