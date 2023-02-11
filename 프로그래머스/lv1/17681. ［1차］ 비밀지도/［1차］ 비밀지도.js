function solution(n, arr1, arr2) {
    const binaryArr1 = convert(arr1);
    const binaryArr2 = convert(arr2);
    const sumArr = binaryArr1.map((num, i) => String(num + binaryArr2[i]));
    const result = sumArr.map((num) => {
        let str = num.split('').map((digit) => digit > 0 ? '#' : ' ').join('');
        if (str.length < n) {
            while(str.length < n) {
                str = ' ' + str;
            }
        }
        return str;
    })
    return result;
}

function convert(arr) {
    return arr.map((num) => Number(num.toString(2)));
}