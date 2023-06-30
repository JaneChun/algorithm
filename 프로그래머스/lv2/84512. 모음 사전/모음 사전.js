function solution(word) {
    const VOWELS = ['A', 'E', 'I', 'O', 'U'];
    const dictionary = [];
    
    const dfs = (str, len) => {
        if (str.length === len) {
            return dictionary.push(str);
        }
        for (let i = 0; i < VOWELS.length; i++) {
            const newStr = str + VOWELS[i];
            dfs(newStr, len, dictionary);
        }
    }
    
    for (let len = 1; len <= VOWELS.length; len++) {
        dfs('', len, dictionary);
    }
    
    dictionary.sort();
    
    return dictionary.indexOf(word) + 1;
}