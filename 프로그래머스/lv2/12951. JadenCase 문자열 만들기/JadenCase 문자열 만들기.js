function solution(s) {
    return s.split(' ').map((str) => str.charAt(0).toUpperCase() + str.slice(1).toLowerCase()).join(' ');
}