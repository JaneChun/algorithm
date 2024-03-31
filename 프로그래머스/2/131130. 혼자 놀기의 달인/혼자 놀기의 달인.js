function solution(cards) {
    const dfs = (idx, visited, count) => {
        if (visited[idx]) return count;
        visited[idx] = true;
        return dfs(cards[idx - 1], visited, count + 1);
    };

    let maxScore = 0;

    for (let i = 0; i < cards.length; i++) {
        const visited = new Array(cards.length + 1).fill(false);
        const score1 = dfs(cards[i], visited, 0); // 4

        const leftCards = cards.filter((_, index) => !visited[index + 1]); // [2,5,6]
        const visited2 = new Array(leftCards.length + 1).fill(false);
        for (j = 0; j < leftCards.length; j++) {
            const score2 = leftCards.length === 0 ? 0 : dfs(leftCards[j], visited2, 0);
            const score = score1 * score2;
            maxScore = Math.max(maxScore, score);
        }
    }

    return maxScore;
}
