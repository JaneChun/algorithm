function solution(survey, choices) {
    const hash = {R: 0, T: 0, C: 0, F: 0, J: 0, M: 0, A: 0, N: 0};
    
    survey.forEach(([disagree, agree], i) => {
        const num = choices[i];
        
        if (num === 4) return false;
        else if (num < 4) hash[disagree] += Math.abs(num - 4);
        else hash[agree] += Math.abs(num - 4);
    })
    
    return ['RT', 'CF', 'JM', 'AN'].map((typePair) => findBigger(typePair, hash)).join('');
}

function findBigger([type1, type2], hash) {
    return hash[type1] < hash[type2] ? type2 : type1;
}