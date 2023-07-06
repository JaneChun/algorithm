function solution(routes) {
    let count = 0;
    let camera = -30001;
    routes.sort((a, b) => a[1] - b[1]);
    
    for (const [enter, out] of routes) {
        if (camera < enter) {
            count++;
            camera = out;
        }
    }
    return count;
}