function solution(s) { // ['b', 'a', 'n', 'a', 'n', 'a']
    return s.split('').map((v, i, arr) => {
        const idx = arr.slice(0, i).lastIndexOf(v);
        return idx === -1 ? -1 : i - idx;
    })
}