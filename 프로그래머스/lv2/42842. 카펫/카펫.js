function solution(brown, yellow) {
    const answer = [0, 0];
    const S = brown + yellow;

    
    for (let width = S; width > 0; width--) {
        if (S % width !== 0) continue;
        
        const height = S / width;
        const yellowS = (width - 2) * (height - 2);
        const brownS = S - yellowS;
        
        if (yellowS === yellow && brownS === brown) {
            answer[0] = width;
            answer[1] = height;
            break;
        }
    }
    
    return answer;
}