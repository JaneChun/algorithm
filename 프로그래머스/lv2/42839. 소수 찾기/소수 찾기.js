function solution(numbers) {
    const set = new Set();
    dfs('', [...numbers], set);
    return set.size;
}

function isPrime(num) {
    if (num <= 1) return false;
    if (num === 2) return true;
    if (num % 2 === 0) return false;
    
    for (let i = 3; i <= Math.floor(Math.sqrt(num)); i += 2) {
        if (num % i === 0) return false;
    }
    return true;
}

function dfs(fixed, rest, set) {
    if (rest.length >= 1) {
        for (let i = 0; i < rest.length; i++) {
            let newFixed = fixed + rest[i];
            let copyArr = [...rest];
            copyArr.splice(i, 1);
            if (isPrime(+newFixed)) set.add(+newFixed);
            
            dfs(newFixed, copyArr, set);
        }
    }
}