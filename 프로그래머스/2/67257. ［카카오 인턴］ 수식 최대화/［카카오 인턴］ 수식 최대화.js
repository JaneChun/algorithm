// function solution(expression) {
//     // 가능한 우선순위 조합
//     const prior = [
//         ['+', '-', '*'],
//         ['+', '*', '-'],
//         ['-', '+', '*'],
//         ['-', '*', '+'],
//         ['*', '-', '+'],
//         ['*', '+', '-']
//     ]
//     let result = [] // 각 우선순위에 따른 계산한 결과를 담아두는 배열
    
//     for (let opArr of prior) { // opArr = ['+', '-', '*']
//         const temp = expression.split(/(\D)/) 
//         // [ '100', '-', '200', '*', '300', '-', '500', '+', '20']
//         for (let op of opArr) { // op = '-'
//             while (temp.includes(op)) {
//                 const idx = temp.indexOf(op) // op의 앞의 숫자, op, op뒤의 숫자를 자르고, 뒤의 걸로 대체한다.
//                 const cal = calculate(temp[idx - 1], op, temp[idx + 1])
//                 temp.splice(idx - 1, 3, cal)
//             }
//         }
//         result.push(Math.abs(temp[0]))
//     }
//     return Math.max(...result)
// }
    
// function calculate(a, op, b) {
//     if (op === '+') return +a + +b
//     if (op === '-') return a - b
//     if (op === '*') return a * b
// }

function solution(expression) {
    const expressions = [
        ['+', '-', '*'],
        ['+', '*', '-'],
        ['-', '+', '*'],
        ['-', '*', '+'],
        ['*', '-', '+'],
        ['*', '+', '-']
    ]
    let max = 0
        
    let tokens = expression.match(/(\d+|[-+*/])/g);
    // ['100', '-','200', '*', '300', '-', '500', '+', '20']
    
    expressions.forEach((ex, i) => { // '+-*'
        let tokens_c = [...tokens] // ['100', '-','200', '*', '300', '-', '500', '+', '20']
        console.log('ex', ex, 'i', i)
        ex.forEach((e) => { // e = '+'
            for (let i = 0; i < tokens_c.length; i++) {
                if (e === tokens_c[i]) { // tokens_c[i] = '+'
                    let temp;
                    if (e === '+') {
                        temp = +tokens_c[i - 1] + +tokens_c[i + 1];
                    } else if (e === '*') {
                        temp = +tokens_c[i - 1] * +tokens_c[i + 1];
                    } else {
                        temp = +tokens_c[i - 1] - +tokens_c[i + 1];
                    }
                    tokens_c.splice(i - 1, 3, temp.toString());
                    i--;
                } 
            }
        });
        max = Math.max(max, Math.abs(Number(tokens_c[0])));
    });
    
    return max
}