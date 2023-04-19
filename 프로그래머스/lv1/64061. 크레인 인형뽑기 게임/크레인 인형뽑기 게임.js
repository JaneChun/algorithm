function solution(board, moves) {
    const stack = [];
    let count = 0;

    moves.forEach((move) => {
        for (let i = 0; i < board[0].length; i++) {
            if (board[i][move - 1] === 0) continue;
            
            if (stack[stack.length - 1] === board[i][move - 1]) {
                stack.pop();
                count += 2;
            } else {
                stack.push(board[i][move - 1]);
            }
            board[i][move - 1] = 0;
            break;
        }
    })
    return count;
}