function solution(n, arr1, arr2) {
    return arr1.map((v, i) => (+v.toString(2) + +arr2[i].toString(2)).toString())
            .map((v) => v.length < n ? '0'.repeat(n - v.length) + v : v) // 부족한 자리수만큼 앞에 0 붙이기
            .map((v) => v.split('').map((v) => v === '0' ? ' ' : '#').join('')) // 0이면 ' ', 아니면 '#'으로 매핑하기  ["0","0","2","2","0"]
    
}
