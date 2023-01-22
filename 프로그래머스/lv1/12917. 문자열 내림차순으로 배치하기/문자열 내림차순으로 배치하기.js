function solution(s) {
    return s.split('').sort((a,b) => a - b).reverse().join('')
}