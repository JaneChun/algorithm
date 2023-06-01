function solution(elements) {
    const sumSet = new Set();

    for (let w = 1; w <= elements.length; w++) { // w는 window의 크기
        let windowSum = 0;
        
        for (let j = 0; j < elements.length; j++) { // 배열 elements를 순회 (j는 창문 시작 인덱스)
            if (j === 0) { // 맨 처음의 창문에 대해서만 직접 합을 구한다.
                for (let k = 0; k < w; k++) { // 창문 안에 있는 요소들을 (w개)
                    windowSum += elements[k]; // windowSum에 더해준다.
                }
            } else { // 이후 창문들은 이전에 계산한 값을 활용한다.
                windowSum -= elements[j - 1]; // 이전 값 빼주기
                windowSum += elements[(j + w - 1) % elements.length]; // 다음 값 더해주기, 원형 수열이므로 % 이용
            }
            sumSet.add(windowSum);
        }
    }
    
    return sumSet.size;
}