function solution(friends, gifts) {
    const giftMap = friends.reduce((acc, giver, i) => {
        acc[giver] = {}
        friends.forEach((receiver, j) => {
            if (i !== j) acc[giver][receiver] = 0
        })
        return acc
    }, {})

    const giftIndex = friends.reduce((acc, name) => {
        acc[name] = 0
        return acc
    }, {})
    
    gifts.forEach((gift) => {
        const [giver, receiver] = gift.split(' ')
        giftMap[giver][receiver]++
        giftIndex[giver]++
        giftIndex[receiver]--
    })
    console.log(giftMap)
    // {
    //   muzi: { ryan: 0, frodo: 2, neo: 0 },
    //   ryan: { muzi: 3, frodo: 0, neo: 0 },
    //   frodo: { muzi: 1, ryan: 1, neo: 0 },
    //   neo: { muzi: 1, ryan: 0, frodo: 0 }
    // }
    
    console.log('giftIndex', giftIndex)
    // giftIndex { muzi: -3, ryan: 2, frodo: 0, neo: 1 }
    
    const nextMonth = friends.reduce((acc, name) => {
        acc[name] = 0
        return acc
    }, {})
    // { muzi: 0, ryan: 0, frodo: 0, neo: 0 }
    
    Object.entries(giftMap).forEach(([giver, receiversObj]) => { // muzi { ryan: 0, frodo: 2, neo: 0 }
        // 두 사람 중 더 많은 선물 준 사람++
        Object.entries(receiversObj).forEach(([receiver, giveCount]) => {
            const receiveCount = giftMap[receiver][giver]
            if (giveCount > receiveCount) nextMonth[giver]++
            else if (giveCount < receiveCount) nextMonth[receiver]++
            else {
                // 선물 지수 높은 사람++
                if (giftIndex[giver] > giftIndex[receiver]) nextMonth[giver]++
                else if (giftIndex[giver] < giftIndex[receiver]) nextMonth[receiver]++
                else return
            }
        })
    })
    
    return Math.max(...Object.values(nextMonth))/2
} 