function solution(array, commands) {
    return commands.map(([start, end, k]) => array.slice(start - 1, end).sort((a, b) => a - b)[k - 1]);
}