function solution(msg) {
    const dict = {};
    const startCharCode = 'A'.charCodeAt(); // 65
    
    for (let i = 0; i < 26; i++) {
        const alphabet = String.fromCharCode(startCharCode + i);
        dict[alphabet] = i + 1;
    }
    
    const result = [];
    let curInput = '';
    
    for (let i = 0; i < msg.length; i++) { // i = 2
        curInput += msg[i]; // curInput = 'A'
        
        while (curInput) {
            if (dict[curInput]) { // false
                result.push(dict[curInput]) // dict = [11]
                return;
            } else {
                dict[curInput] = Object.keys(dict).length + 1; // dict['KA'] = 27
                curInput = msg[i]; // curInput = 'A'
            }    
        }
    }
    console.log('dict', dict)
    return result;
}