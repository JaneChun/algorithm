function solution(s) {
    let counter = 0;
    result = '';
    
    for (let i = 0; i < s.length; i++) {
        if (s[i] === ' ') {
            result = result + ' ';  
            counter = 0;
        } else {
            if(counter % 2 === 0) {
                result = result + s[i].toUpperCase();
            } else {
                result = result + s[i].toLowerCase();
            }
            counter++;
        }
    }
    return result;
}