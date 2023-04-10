function solution(n, lost, reserve) {
    const filteredReserve =  reserve.filter((v) => !lost.includes(v)).sort((a, b) => a - b);
    const filteredLost = lost.filter((v) => !reserve.includes(v)).sort((a, b) => a - b);
    
    return n - filteredLost.map((v) => {
        const borrowFromFront = filteredReserve.indexOf(v - 1);
        const borrowFromBack = filteredReserve.indexOf(v + 1);
        
        if (borrowFromFront !== -1) {
            filteredReserve.splice(borrowFromFront, 1);
            return null;
        } else if (borrowFromBack !== -1) {
            filteredReserve.splice(borrowFromBack, 1);
            return null;
        } else {
            return v;    
        }
        
    }).filter((v) => v).length;
}