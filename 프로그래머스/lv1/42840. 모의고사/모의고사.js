function solution(answers) {
    const result = [];
    const one = [1, 2, 3, 4, 5],
          two = [2, 1, 2, 3, 2, 4, 2, 5],
          three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5];
    
    let score = [0, 0, 0];
    
    answers.forEach((v, i) => {
        if (v === one[i % 5]) score[0]++;
        if (v === two[i % 8]) score[1]++;
        if (v === three[i % 10]) score[2]++;
    })
    
    const max = Math.max(...score);
   
    score.forEach((v, i, arr) => v === max ? result.push(i + 1) : v);
   
    return result;
}