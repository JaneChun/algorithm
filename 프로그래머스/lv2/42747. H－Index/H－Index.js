function solution (citations) {      // citations = [3, 0, 6, 1, 5]
    citations.sort((a, b) => b - a); // 내림차순으로 정렬 [6, 5, 3, 1, 0]
                                    
    
    for (let i = 0; i < citations.length; ++i) { // i = 0, 1, 2, 3, 4
        let hIndex = citations[i];          // hIndex = 6, 5, 3, 1, 0
        if (i + 1 > hIndex) {               // i + 1 = 1, 2, 3, 4, 5
            return i;
        }
        
    }
    return citations.length;
}

// h번 이상 인용된 논문이 몇 편 있는지 나타내는 i, 1씩 증가 
// 이때 h번 인용되었음을 나타내는 수는 citations[i]

// hIndex가 6이 되려면, 6번 이상 인용된 논문이 6편 이상이어야 한다. -> 1편이므로 X
// hIndex가 5가 되려면, 5번 이상 인용된 논문이 5편 이상이어야 한다. -> 2편이므로 X
// hIndex가 3이 되려면, 3번 이상 인용된 논문이 3편 이상이어야 한다. -> 3편이므로 O




