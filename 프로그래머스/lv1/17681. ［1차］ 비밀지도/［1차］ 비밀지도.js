function solution(n, arr1, arr2) {
    return arr1.map((v, i) => addZero(n, (v | arr2[i]).toString(2)).replace(/1/g,'#').replace(/0/g, ' '));
}

function addZero(n, str){
    return '0'.repeat(n - str.length) + str;
}