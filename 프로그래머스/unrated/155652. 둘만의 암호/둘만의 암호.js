function solution(s, skip, index) {
    const set = new Set('abcdefghijklmnopqrstuvwxyz');
    skip.split('').forEach((char) => set.delete(char));
    const arr = [...set];
    return s.split('').map((char) => {
        const newIdx = arr.indexOf(char) + index;
        console.log(newIdx)
        return arr[newIdx % set.size];
    }).join('');
}