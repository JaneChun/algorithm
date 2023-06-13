function solution(participant, completion) {
    const map = new Map();
    
    participant.forEach((name) => map.set(name, (map.get(name) || 0) + 1));
    completion.forEach((name) => map.set(name, (map.get(name) || 0) - 1));

    for(const [key, value] of map) {
        if (value > 0) return key;
    }
}