function solution(numbers, hand) {
    let left = 10; // *
    let right = 11; // #
    
    return numbers.reduce((acc, num) => {
        if (num % 3 === 1) {
            left = num;
            console.log('left', left)
            return acc + 'L';
        } else if (num % 3 === 0 && num !== 0) {
            right = num;
            console.log('right', right)
            return acc + 'R';
        } else {
            const distance = distanceFromNum(num);
            console.log(distance)
            if (distance[left] === distance[right]) {
                hand === 'left' ? left = num : right = num;
                return hand === 'left' ? acc + 'L' : acc + 'R';
            } else if (distance[left] < distance[right]) {
                left = num;
                 console.log('left', left)
                return acc + 'L'
            } else {
                right = num;
                console.log('right', right)
                return acc + 'R'
            };
        }
        
    }, '');
}

function distanceFromNum (num) {
    switch (num) {
        case 2:
            return [3, 1, 0, 1, 2, 1, 2, 3, 2, 3, 4, 4];
        case 5:
            return [2, 2, 1, 2, 1, 0, 1, 2, 1, 2, 3, 3];
        case 8:
            return [1, 3, 2, 3, 2, 1, 2, 1, 0, 1, 2, 2];
        case 0:
            return [0, 4, 3, 4, 3, 2, 3, 2, 1, 2, 1, 1];
    }
}
                          