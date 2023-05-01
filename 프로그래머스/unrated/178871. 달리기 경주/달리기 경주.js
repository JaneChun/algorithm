function solution(players, callings) {
    const map = new Map();
    players.forEach((player, i) => map.set(player, i));
    // { mumu: 0, soe: 1, poe: 2, kai: 3, mine: 4 }
    
    callings.forEach((player) => {
        const prevRanking = map.get(player); // 3
        const passedPlayer = players[prevRanking - 1]; // 추월당한 선수
        
        // 배열 업데이트
        players[prevRanking] = passedPlayer;
        players[prevRanking - 1] = player;
        
        // hash 업데이트
        map.set(passedPlayer, prevRanking);
        map.set(player, prevRanking - 1);
    })
    return players;
}