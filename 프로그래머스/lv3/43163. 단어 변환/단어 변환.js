function solution(begin, target, words) {
    if (!words.includes(target)) return 0;
        
    const visited = Array(words.length).fill(false);
    let min = 50;

    const dfs = (begin, target, depth) => {
        if (begin === target) {
            min = Math.min(min, depth);
            return;
        }
        
        for (let i = 0; i < words.length; i++) {
            const word = words[i];
            if (!visited[i] && isChangable(begin, word)) {
                visited[i] = true;
                depth += 1;
                dfs(word, target, depth); 
                visited[i] = false;
                depth -= 1;
            }    
        }
    }
    
    dfs(begin, target, 0);
    
    return min;
}

const isChangable = (from, to) => {
    let diff = 0;
    for (let i = 0; i < from.length; i++) {
        if (from[i] !== to[i])  diff++;
    }
    if (diff === 1) return true;
    else return false;
}