function solution(people, limit) {
    people.sort((a, b) => a - b); // 50 70
    let boats = 0;
    
    while(people.length > 0) {
        const heaviest = people.pop(); // 80
        const lightest = people[0]; // 50
        
        if (lightest + heaviest <= limit) {
            people.shift();
        }
        boats++;
    }
    
    return boats;
}