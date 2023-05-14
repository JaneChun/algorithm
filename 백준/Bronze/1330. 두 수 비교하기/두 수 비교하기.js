const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
const [A, B] = fs.readFileSync(filePath).toString().split(' ');

console.log(+A === +B ? '==' : +A > +B ? '>' : '<');