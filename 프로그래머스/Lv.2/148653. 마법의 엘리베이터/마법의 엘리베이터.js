function solution(storey) {
    let count = 0
    
    while (storey) {
        let cur = storey % 10
        let next = parseInt(storey / 10) % 10
        
        if (cur > 5) {
            count += (10 - cur) // 5보다 크면 10까지 올라감
            storey += 10
        } else if (cur === 5) { // 5면 5번 누름
            count += cur
            storey += (next >= 5 ? 10 : 0) // 다음 층이 5보다 크면 10으로 올라가고, 아니면 내려감
        } else { // 5보다 작으면 0까지 내려감
            count += cur
        }
        
        storey = parseInt(storey / 10) // 자릿수 변경
    }
    
    return count
}