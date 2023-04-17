function solution(babbling) {
    let count = 0;
    
    babbling.forEach((string) => { // 'ayaye'
        const regex = /(aya|ye|woo|ma)/g;
        const matches = string.match(regex); // ['aya', 'ye']
        
        if (!matches)  return; // 
        
        let prev = ''
        matches.forEach((match) => { // 'aya'
            if (prev === match) return;
            string = string.replace(match, ''); // 문자열에서 match 잘라내기
            prev = match;
        });

        if (string === '') count++;        
    })
    
    return count;
}