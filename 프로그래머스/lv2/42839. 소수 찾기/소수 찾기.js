function solution(numbers) {
    const set = new Set();
    dfs('', [...numbers], set);
    return set.size;
}

// fixed : 고정된 문자열
// rest : 고정된 문자열을 제외한 값이 담긴 배열
// set : 값을 저장할 Set 객체
function dfs(fixed, rest, set) { // '1', [2, 3], set
    if (rest.length >= 1) {
        for (let i = 0; i < rest.length; i++) { // i = 1
            let newFixed = fixed + rest[i]; // newFixed = '13'
            let copyArr = [...rest]; // [2]
            copyArr.splice(i, 1);
            if (isPrime(+newFixed)) set.add(+newFixed); // set에 넣을 때는 숫자
            
            dfs(newFixed, copyArr, set); // 1, [2, 3], []
        }
    }
}

// dfs([1, 2, 3], '')을 호출하면 dfs가 호출되는 순서

// dfs('', [1, 2, 3])
//  ㄴ dfs('1', [2, 3])     -> fixed = '',   i = 0일 때 (1 depth)
//     ㄴ dfs('12', [3])    -> fixed = '1',  i = 0일 때 (2 depth)
//        ㄴ dfs('123', []) -> fixed = '12', i = 0일 때 (3 depth)
//     ㄴ dfs('13', [2])    -> fixed = '1',  i = 1일 때 (2 depth)
//        ㄴ dfs('132', []) -> fixed = '13', i = 0일 때 (3 depth)
//  ㄴ dfs('2', [1, 3])     -> fixed = '',   i = 1일 때 (1 depth)
//      ㄴ dfs('21', [3])   -> fixed = '2',  i = 0일 때 (2 depth)
//        ㄴ dfs('213', []) -> fixed = '21', i = 0일 때 (3 depth)
//      ㄴ dfs('23', [1])   -> fixed = '2',  i = 1일 때 (2 depth)
//        ㄴ dfs('231', []) -> fixed = '23', i = 0일 때 (3 depth)
// ...

function isPrime(num) {
    if (num <= 1) return false; // 0, 1은 소수가 아님
    if (num === 2) return true; // 2는 소수임
    if (num % 2 === 0) return false; // 짝수는 소수가 아님
    
    for (let i = 3; i <= Math.floor(Math.sqrt(num)); i += 2) {
        if (num % i === 0) return false;
    }
    return true;
}