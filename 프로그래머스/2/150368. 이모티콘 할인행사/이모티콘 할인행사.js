function solution(users, emoticons) {
    const result = { register: -Infinity, cost: -Infinity }
    const discounts = [10, 20, 30, 40]
    
    users = users.map(([discountRate, maxCost]) => ({discountRate, maxCost}))
    // 	[
    //   { discountRate: 40, maxCost: 10000 },
    //   { discountRate: 25, maxCost: 10000 }
    // ] 
    
    // 각 사용자의 이모티콘 구매 비용 합계
    const userTotalCost = Array.from({length: users.length}).fill(0) // [0, 0, 0, 0]
    
    // 이모티콘의 가격을 할인율에 따라 계산해주는 함수
    const getCost = (idx, rate) => {
        return emoticons[idx] * (100 - rate) / 100
    }
    
    const dfs = (emoticonIdx) => { // emoticonIdx = 0
        if (emoticonIdx === emoticons.length) { // base case : 모든 이모티콘에 할인율을 적용한 경우 종료
            let maxRegister = 0 // 이모티콘 플러스 가입자수 초기화
            let maxCost = 0     // 이모티콘 판매액 초기화
           
            // 각 사용자에 대해 처리
            for (let i = 0; i < users.length; i++) {
                // 사용자는 자신의 구매 한도보다 구매 비용의 합이 크다면 이모티콘 플러스에 가입한다.
                if (users[i].maxCost <= userTotalCost[i]) {
                    maxRegister++
                // 자신의 구매 한도보다 구매비용의 합이 작다면 이모티콘을 개별로 구매한다.
                } else {
                    maxCost += userTotalCost[i]
                }
            }
            
            // 현재까지의 최대 결과와 비교하여 업데이트
            if (result.register < maxRegister || result.register === maxRegister && result.cost <= maxCost) {
                result.register = maxRegister
                result.cost = maxCost
            }
            
            return
        }
        
        // 모든 할인율에 대해 구매 시도
        for (let i = 0; i < 4; i++) {
            const discountRate = discounts[i]

            // 각 사용자에 대해 사용자가 원하는 할인율보다 할인율이 높다면 구매
            for (let j = 0; j < users.length; j++) {
                if (users[j].discountRate <= discountRate) {
                    userTotalCost[j] += getCost(emoticonIdx, discountRate)
                    }
                }

            // 다음 이모티콘에 대해 dfs 호출
            dfs(emoticonIdx + 1)

            // 이모티콘 구매 비용 초기화
            for (let j = 0; j < users.length; j++) {
                if (users[j].discountRate <= discountRate) {
                    userTotalCost[j] -= getCost(emoticonIdx, discountRate)
                    }
                }
            }       
        }
    
    dfs(0)
    
    return [result.register, result.cost]
}