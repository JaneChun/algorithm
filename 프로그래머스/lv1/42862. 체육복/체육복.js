function solution(n, lost, reserve) {
    const reserveSelf = reserve.filter((v) => !lost.includes(v)).sort((a, b) => a - b);
    const selfArr = lost.filter((v) => !reserve.includes(v)).sort((a, b) => a - b);
    
    return n - selfArr.map((v) => {
        // const borrowFromSelf = reserve.indexOf(v);
        const borrowFromFront = reserveSelf.indexOf(v - 1);
        const borrowFromBack = reserveSelf.indexOf(v + 1);
        
        // if (borrowFromSelf !== -1) {
        //     reserve.splice(borrowFromSelf, 1);
        //     console.log(reserve);
        //     return null;
        // } else 
            if (borrowFromFront !== -1) {
            reserveSelf.splice(borrowFromFront, 1);
            console.log(reserveSelf);
            return null;
        } else if (borrowFromBack !== -1) {
            reserveSelf.splice(borrowFromBack, 1);
            console.log(reserveSelf);
            return null;
        } else {
            return v;    
        }
        
    }).filter((v) => v).length
}