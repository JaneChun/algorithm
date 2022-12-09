function solution(A, B){
// A = [1, 4, 2] , B = [5, 4, 4]
// 두 배열을 sort 하면
// [1, 2, 4], [4, 5, 5] = 4 + 10 + 20
// 순서대로 곱하기
    let result = 0;
    A.sort((a, b) => a - b);
    B.sort((a, b) => b - a);
    
    for(let i = 0; i < A.length; i++) {
       result += A[i] * B[i];
   }
    return result;
}