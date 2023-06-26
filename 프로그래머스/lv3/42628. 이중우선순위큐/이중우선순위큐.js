function solution(operations) {
    const queue = [];
    operations = operations.map((str) => str.split(' '));
    
    for (const [command, num] of operations) {
        if (command === 'I') {
            queue.push(num);
        } else {
            if(queue.length === 0) continue;
            num === '1' ? queue.sort((a, b) => a - b) : queue.sort((a, b) => b - a);
            queue.pop();
        }
    }
    
    const max = queue.length ? Math.max(...queue) : 0;
    const min = queue.length ? Math.min(...queue) : 0;
    return [max, min];
}