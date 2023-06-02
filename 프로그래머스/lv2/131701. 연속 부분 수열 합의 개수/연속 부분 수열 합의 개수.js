function solution(elements) {
    const sumSet = new Set();
    const len = elements.length;

    for (let w = 1; w <= len; w++) { // w는 window의 크기 // w = 1, 2, 3, 4, 5
        let windowSum = 0;
        
        for (let i = 0; i < len; i++) { // 배열 순회 i = 0, 1, 2, 3, 4
            if (i === 0) { // 첫번째만 계산해줌
                for (let j = 0; j < w; j++) { // 창문 크기만큼 반복문으로 더하기
                    windowSum += elements[j];
                }
            } else { // 그 뒤의 경우에는
                windowSum -= elements[i - 1];
                windowSum += elements[(i + w - 1) % len];
            }
            sumSet.add(windowSum);
        }
    }
    
    return sumSet.size;
}