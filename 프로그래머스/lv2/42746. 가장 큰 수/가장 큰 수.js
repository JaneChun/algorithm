function solution(numbers) { // numbers = [3, 30, 34, 5, 9]
    let strings = numbers.map((num) => String(num)); // strings = ['3', '30', '34', '5', '9']
    strings.sort((a, b) => (b + a) - (a + b));       // strings = ['9', '5', '34', '3', '30']
    // 만약 a = '3', b = '30'일 때
    // (b + a) - (a + b) = '303' - '330' = -27로, 
    //  330이 앞에 오고, 303이 뒤에 오는 것이 더 큰 수를 만들 수 있다.
    
    // 만약 a = '30', b = '34일' 때
    // (b + a) - (a + b) = '3430' - '3034' = 396으로, 
    // 34가 앞에 오고, 30이 뒤에 오는 것이 더 큰 수를 만들 수 있다.
    
    const answer = strings.join(''); // '9534330'
    
    return answer[0] === "0" ? "0" : answer; // 만약 answer가 '0____'으로 시작하면 0을 리턴하도록 조건
}