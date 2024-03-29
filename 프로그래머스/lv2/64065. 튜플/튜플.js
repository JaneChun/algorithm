function solution(s) {
    const result = [];// 3 2 4 1
    const tuples = s.slice(2, -2).split('}\,{')
                              .sort((a, b) => a.length - b.length);
    
    tuples.forEach((tuple) => {
        tuple = tuple.split(',');
        result.push(tuple.find((el) => !result.includes(el)));
    })
    
    return result.map((str) => Number(str));
}
