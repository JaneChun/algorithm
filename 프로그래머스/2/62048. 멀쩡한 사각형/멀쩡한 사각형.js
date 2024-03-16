function solution(w, h) {
    function getGCD(a, b) {
      if (b === 0) return a;
      return getGCD(b, a % b);
    }
    
    // 패턴의 개수
    const gcd = getGCD(w, h)
    const x = w / gcd
    const y = h / gcd
    const patternCount = w / x
    console.log(patternCount) // 4
    
    // 패턴이 차지하는 사각형 개수
    let unusable
    if (x === y) unusable = x
    else unusable = x + y - 1
    
    return w * h - patternCount * unusable
}
// 패턴의 종료지점
// 2, 3
// 4, 6
// 6, 9
// 8, 12 (+ 2, + 3씩 증가)
// 규칙 : W와 H의 최대공약수 4로 W와 H를 각각 나누면 몫이 각각 2, 3임

// 패턴이 차지하는 사각형 개수
// 패턴이 1*1 일 때 - 1개
// 패턴이 1*2 일 때 - 2개
// 패턴이 2*2 일 때 - 2개
// 패턴이 2*3 일 때 - 4개
// 패턴이 3*4 일 때 - 6개
// 규칙 : 정사각형일 때는 x개
//       직사각형일 때는 x + y - 1개
