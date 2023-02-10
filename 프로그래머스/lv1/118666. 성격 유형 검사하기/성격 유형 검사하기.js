function solution(survey, choices) {
    const hash = {};
    const types = ['RT', 'CF', 'JM', 'AN'];
    
    types.forEach((type) => type.split('').forEach((char) => hash[char] = 0));
    
    choices.forEach((choice, i) => {
        const [disagree, agree] = survey[i];
        hash[choice < 4 ? disagree : agree] += Math.abs(4 - choice);
    });
    
    // hash = {'R': 6, 'T': 1 ...}
    // type = 'RT'
    return types.map(([a, b]) => hash[a] >= hash[b] ? a : b).join('');
}