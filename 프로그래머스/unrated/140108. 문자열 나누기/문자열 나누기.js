function solution(s) {
    let char = s[0];
    let charCount = 0, otherCount = 0, splitCount = 0;
    
    for (let i = 0; i < s.length; i++) {
        if (s[i] === char) charCount++;
        else otherCount++;
        
        if (charCount === otherCount) {
            splitCount++;
            char = s[i + 1];
            charCount = 0, otherCount = 0;
        } else {
            i === s.length - 1 && splitCount++;
        }
    }
    
    return splitCount;
}