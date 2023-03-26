function solution(nums) {
    const get = nums.length / 2;
    const unique = [...new Set(nums)];

    return unique.length > get ? get : unique.length;
}