function solution(s) {
    
    let convertCount = 0;
    let zeroCount = 0;
    
    const removeZero = (str) => {
        let result = '';
        
        for (let i = 0; i < str.length; i++) {
        
            if (str[i] === "1") {
                result = result + str[i];
            } else {
                zeroCount++;
            }
        } // result = "111111"
        result = result.length.toString(2); // result = "110"
        convertCount++;
        
        if (result === "1") {
            return [convertCount, zeroCount]
        } else {
            return removeZero(result); // removeZero("110");
        }
    }
    
    return removeZero(s);
}

// solution("110010101001") - 이진변환 1번
// "111111" - 0 제거
// 길이 6
// "110" - 6을 이진변환 2번
// "11" - 0 제거
// 길이 2
// "10" - 2를 이진변환 3번
// "1" - 0 제거

// -> [3, 8] 리턴