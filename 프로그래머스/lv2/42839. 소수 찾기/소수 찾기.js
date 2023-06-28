function solution(numbers) {
    const perArr = getPermutations(numbers.split(''));
    
    const set = new Set();
    perArr.map((arr) => set.add(Number(arr.join(''))));
    console.log(set); // { 17, 71 }
    
    let countOfPrimeNumbers = 0;
    for (const num of set) {
        // 소수면
        console.log(num, isPrimeNumber(num))
        if (isPrimeNumber(num)) countOfPrimeNumbers++;
    }
    return countOfPrimeNumbers;
}

function isPrimeNumber(num) {
    if (num <= 1) return false; // 0, 1은 소수가 아님
    if (num === 2) return true; // 2는 소수임
    if (num % 2 === 0) return false; // 짝수는 소수가 아님
    
    for (let i = 3; i <= Math.floor(Math.sqrt(num)); i += 2) {
        if (num % i === 0) {
            return false;
        }
        return true;
    }
    return true;
}

function getPermutations(arr) {
    const result = [];
    arr.forEach((num) => result.push([num])); // 요소 하나로 이루어진 숫자도 추가해야하므로
    
    const dfs = (i, arr) => {
        if (i === arr.length) {
            return result.push([...arr]);
        }

        for (let j = i; j < arr.length; j++) {
            [arr[i], arr[j]] = [arr[j], arr[i]];
            dfs(i + 1, arr);
            [arr[i], arr[j]] = [arr[j], arr[i]];
        }
    }
    
    dfs(0, arr);
    
    return result;
}