function solution(s, n) {
    const upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
    const lower = 'abcdefghijklmnopqrstuvwxyz';
    
    return s.split('')
            .map((v) => v === ' ' ? v : (
                v === v.toUpperCase() ? 
                upper[(upper.indexOf(v) + n) % upper.length] : 
                lower[(lower.indexOf(v) + n) % lower.length])
            ).join('');
}
