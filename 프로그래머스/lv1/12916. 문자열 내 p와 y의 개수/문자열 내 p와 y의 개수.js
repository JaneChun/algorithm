function solution(s){
    const flat = s.toLowerCase(); // "ppoooyy"
    let p = 0;
    let y = 0;
    for(let i = 0; i < flat.length; i++) {
       if (flat[i] === 'p') {
           p++;
       } else if (flat[i] === 'y') {
           y++;
       } 
    }
    
    return p === y;
}