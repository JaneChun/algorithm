function solution(s){
    let p = 0;
    let y = 0;
    s.toLowerCase().split('').forEach((v) => v === 'p' ? p++ : (v === 'y' ? y++ : v));

    return p === y;
}