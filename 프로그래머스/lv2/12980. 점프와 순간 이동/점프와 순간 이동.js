function solution(n) {
    let jump = 0;
    
    while (n > 0) {
        if (n % 2 === 0) { // 순간이동 할 수 있는 경우
            n = n / 2;
        } else {
            n -= 1; // 점프 1칸
            jump++; // 점프 횟수
        }
    }
    return jump;
}

// 점프를 하면 1칸당 건전지 1 사용
// 순간이동은 지금까지 온 거리 * 2

// n -> n / 2