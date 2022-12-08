function solution(array, commands) {
    let result = []; // 정답을 모아둘 배열
    
    for (let i = 0; i < commands.length; i++) {
        const command = commands[i];
        let from = command[0] - 1;
        let to = command[1];
        let loc = command[2] - 1;
        
        const slicedArr = array.slice(from, to).sort((a, b) => a - b);
        result.push(slicedArr[loc]);
    }
    
    return result;
}

// 입력값 [1, 5, 2, 6, 3, 7, 4], [i 2, j 5, k 3] => 5
// slicedArr = arr.slice(i - 1, j) // [5, 2, 6, 3]
// slicedArr.sort((a, b) => a - b) // [2, 3, 5, 6]
// return slicedArr[k - 1] // 5