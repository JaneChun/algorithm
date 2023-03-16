function solution(strings, n) {
    return strings.sort((a, b) => {
        if (a.charCodeAt(n) < b.charCodeAt(n)) return -1;
        if (a.charCodeAt(n) > b.charCodeAt(n)) return 1;
        
        return a < b ? -1 : 1;
    });

}