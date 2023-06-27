function solution(priorities, location) {
    let numOfCompletedProcess = 0;
    
    while(priorities.length > 0) {
        const max = Math.max(...priorities);
        const process = priorities.shift();
        if (process === max) { // 현재 프로세스가 최고 우선순위인 경우
            numOfCompletedProcess++;
            if (location === 0) return numOfCompletedProcess; // 현재 프로세스가 찾는 값이고 최고 우선순위인 경우
        } else { // 현재 프로세스가 최고 우선순위가 아닌 경우
            priorities.push(process); // 맨 뒤에 다시 추가
        }
        
        location > 0 ? location -= 1 : location += priorities.length - 1; // 인덱스가 0 이상인 경우 -1 해주고, 0일 경우 맨 뒤 인덱스로 다시 지정해준다.
    }
}