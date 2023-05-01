function solution(players, callings) {
    const hash = {};
    players.forEach((player, i) => hash[player] = i);
    // { mumu: 0, soe: 1, poe: 2, kai: 3, mine: 4 }
    
    callings.forEach((player) => {
        const prevRanking = hash[player]; // 3
        const passedPlayer = players[prevRanking - 1]; // 추월당한 선수
        
        // 배열 업데이트
        players[prevRanking] = passedPlayer;
        players[prevRanking - 1] = player;
        
        // hash 업데이트
        hash[passedPlayer] = prevRanking;
        hash[player] = prevRanking - 1;
    })
    return players;
}