function solution(survey, choices) {
    const hash = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0}
    for (let i = 0; i < choices.length; i++) {
        if (choices[i] < 4) {
            const char = survey[i][0];
            hash[char] = hash[char] + (4 - choices[i]); 
        } else if (choices[i] > 4) {
            const char = survey[i][1];
            hash[char] = hash[char] + (choices[i] - 4);
        }
    }
    
    const result = [];
    const pair = ['RT', 'CF', 'JM', 'AN'];
    for(let i = 0; i < pair.length; i++) {
        const first = pair[i][0];
        const second = pair[i][1];
        const biggerOne = compare(first, hash[first], second, hash[second]);
        result.push(biggerOne);
    }
    
    return result.join('');
}

function compare(key1, val1, key2, val2) {
    if (val1 >= val2) return key1;
    else return key2;
}