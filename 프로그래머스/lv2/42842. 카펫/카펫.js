function solution(brown, yellow) { // 10, 2
    const answer = [0, 0];
    const S = brown + yellow; // 전체 면적 S = 12
    
    for (let width = S; width > 0; width--) { // width = 4
        if (S % width !== 0) continue; // 전체 면적이 너비로 나누어떨어지지 않는 경우는 스킵
        
        const height = S / width;                   // height = 3
        const yellowS = (width - 2) * (height - 2); // 2 * 1 = 2
        const brownS = S - yellowS;                 // 10
        
        if (yellowS === yellow && brownS === brown) { // 조건이 맞아 떨어지면
            answer[0] = width;
            answer[1] = height;
            break; // 반복문 탈출
        }
    }
    
    return answer;
}