function solution(numbers) { // numbers = [3, 30, 34, 5, 9]
    let strings = numbers.map((num) => String(num)); // strings = ['3', '30', '34', '5', '9']
    strings.sort((a, b) => (b + a) - (a + b));       // strings = ['9', '5', '34', '3', '30']
    const answer = strings.join(''); // '9534330'
    return answer[0] === "0" ? "0" : answer;
}