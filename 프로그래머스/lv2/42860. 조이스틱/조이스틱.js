function solution(name) {
    let click = 0;
    let minMove = name.length - 1;

    for (let i = 0; i < name.length; i++) {
        click += Math.min(name.charCodeAt(i) - 65, 91 - name.charCodeAt(i));
        
        let nextIdx = i + 1;
        while (name[nextIdx] && name[nextIdx] === 'A') {
            nextIdx++;
        }

        minMove = Math.min(
            minMove,
            (i * 2) + name.length - nextIdx,
            ((name.length - nextIdx) * 2) + i
        )
    }
    
    return click + minMove;
}