function solution(people, limit) {
    people.sort((a, b) => a - b);
    let boats = 0;
    
    while(people.length > 0) {
        const heaviest = people.pop();
        const lightest = people[0];
        
        if (lightest + heaviest <= limit) {
            people.shift();
        }
        boats++;
    }
    
    return boats;
}