function solution(n, words) {
    const hash = {};
    
    for (let i = 0; i < words.length; i++) {
        const word = words[i];
        const prev = words[i - 1];
        
        if ((i > 0 && word[0] !== prev[prev.length - 1]) || hash[word]) {
            const number = (i + 1) % n === 0 ? n : (i + 1) % n;
            const turn = Math.ceil((i + 1) / n);
            return [number, turn];
        } else { // hash[word] === undefined
            hash[word] = true;
        }
    }
    
    return [0, 0];
}