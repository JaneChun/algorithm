function solution(nums) {
    const sums = [];
    
    for (let i = 0; i < nums.length; i++) {
        for (let j = i + 1; j < nums.length; j++) {
            for (let k = j + 1; k < nums.length; k++) {
                sums.push(nums[i] + nums[j] + nums[k]);
            }
        }
    }
    
    return sums.filter(isPrimeNumber).length;
}

function isPrimeNumber(num) {
    if (num === 1) return false;
    if (num === 2) return true;
    if (num % 2 === 0) return false;
    for (let i = 3; i <= Math.sqrt(num); i+=2) {
        if (num % i === 0) return false;
    }
    return true;
}