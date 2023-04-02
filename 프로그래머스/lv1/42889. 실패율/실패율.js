function solution(N, stages) {
    const arr = new Array(N).fill(0);
    for (let i = 1; i <= N; i++) {
        let prev = stages.length;
        stages = stages.filter((v) => v !== i)
        arr[i - 1] = {
                        failure : 1 - stages.length / prev,
                        index: i
                     };
    }
    return arr.sort((a, b) => b.failure - a.failure).map((v) => v.index);
}