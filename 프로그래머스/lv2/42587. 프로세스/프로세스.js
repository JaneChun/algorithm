function solution(priorities, location) {
    let numOfCompletedProcess = 0;
    
    while(priorities.length > 0) {
        const max = Math.max(...priorities);
        const process = priorities.shift();
        if (process === max) {
            numOfCompletedProcess++;
            if (location === 0) return numOfCompletedProcess;
        } else {
            priorities.push(process);
        }
        
        location > 0 ? location -= 1 : location += priorities.length - 1
    }
}