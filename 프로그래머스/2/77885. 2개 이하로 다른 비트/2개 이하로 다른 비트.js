function solution(numbers) {
    return numbers.map((number) => { 
        if (number % 2 === 0) {
            return number + 1
        } else {
            const binaryNumber = '0' + number.toString(2)
            const idx = binaryNumber.lastIndexOf('01')
            return parseInt(binaryNumber.substring(0, idx) + '10' + binaryNumber.substring(idx + 2), 2)
        }
    })
}

// function solution(numbers) {
//     return numbers.map((number) => {
//         const binaryNumber = number.toString(2)
//         let nextNumber = number + 1
        
//         while(true) {
//             const binaryNextNumber = nextNumber.toString(2)
            
//             let count = 0
//             for (let i = 1; i <= binaryNextNumber.length; i++) { // 1010 vs 111
//                 if (binaryNextNumber.at(-i) !== binaryNumber.at(-i)) count++
//             }
    
//             if (count <= 2) break
//             nextNumber++
//         }
//         return nextNumber
//     })
// }