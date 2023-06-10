function solution(clothes) {
    const hash = {};
    clothes.forEach(([name, type]) => !hash[type] ? hash[type] = [name] : hash[type].push(name));
    
    return Object.values(hash).reduce((acc, arr) => acc * (arr.length + 1), 1) - 1;
}