function solution(r1, r2) {
    let result = 0
    
    for (let x = 1; x <= r2; x++) { // x = 0 제외한 이유는 *4 할 때 개수가 중복되지 않게 하기 위함
        let maxY = Math.floor(Math.sqrt(r2*r2 - x*x)) 
        // x = 1일 때 : 9 - 1 = √8 = 2.xx = 2 
        // x = 2일 때 : 9 - 4 = √5 = 2.xx = 2
        // x = 3일 때 : 9 - 9 = 0
        let minY = r1 <= x ? 0 : Math.ceil(Math.sqrt(r1*r1 - x*x)) 
        // x = 1일 때 : 4 - 1 = √3 = 1.xx = 2
        // x = 2일 때 : 4 - 4 = √0 = 0
        // x = 3일 때 : 0
        // console.log('x = ', x, '일 때 : y = ', maxY, ' ~ ', minY)
        
        result += maxY - minY + 1
    }
    
    return result * 4
}

// 시간초과
// function solution(r1, r2) {
//     let result = 0;
//     for (let x = -r2; x <= r2; x++) {
//         for (let y = -r2; y <= r2; y++) {
//             if (Math.sqrt(Math.pow(x, 2) + Math.pow(y, 2)) >= r1 && Math.sqrt(Math.pow(x, 2) + Math.pow(y, 2)) <= r2) {
//                 result++;
//             }
//         }
//     }
//     return result;
// }