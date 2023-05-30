function solution(n) {
    let count = 0;
    let sum = 1;
    let left = 1;
    let right = 2;
    while (left <= n) {
        if (sum === n) {
            count++;
            sum -= left;
            left++;
        } else  if (sum < n) {
            sum += right;
            right++;
        } else if (sum > n) {
            sum -= left;
            left++;
        }
    }
    return count;
}