function solution(elements) {
    const sumSet = new Set();
    const len = elements.length;

    for (let w = 1; w <= len; w++) { // w는 window의 크기 // w = 1, 2, 3, 4, 5 (창문 크기)
        let windowSum = 0;
        
        for (let i = 0; i < len; i++) { // 배열 순회 i = 0, 1, 2, 3, 4 어디서부터 더하느냐 (시작점)
            if (i === 0) { // 첫번째만 계산해줌
                for (let j = 0; j < w; j++) { // 창문 크기만큼 반복문으로 더하기 3 (창문개수만큼 시작점 시작해서 더한다)
                    windowSum += elements[j]; // 7
                }
            } else { // 그 뒤의 경우에는
                windowSum -= elements[i - 1]; // 7 - 7
                windowSum += elements[(i + w - 1) % len]; // 0 + 9
            }
            sumSet.add(windowSum); // {7, 9}
        }
    }
    
    return sumSet.size;
}