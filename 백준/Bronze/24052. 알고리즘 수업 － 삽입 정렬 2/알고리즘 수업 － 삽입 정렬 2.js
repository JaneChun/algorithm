const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().split('\n');

const k = Number(input[0].split(' ')[1]);
const arr = input[1].split(' ').map(el => Number(el));

function insertionSort(arr, k) {
  let counter = 0;

  for (let i = 1; i < arr.length; i++) {
    let loc = i - 1;
    let newItem = arr[i];

    while (loc >= 0 && newItem < arr[loc]) {
      arr[loc + 1] = arr[loc];
      loc--;
      counter++;

      if (counter === k) return arr.join(' ');
    }

    // arr[loc] < newItem인 경우
    if (loc + 1 !== i) {
      // i의 값이 변경됐을 때,
      arr[loc + 1] = newItem;
      counter++;
    }

    if (counter === k) return arr.join(' ');
  }
  return -1;
}

console.log(insertionSort(arr, k));