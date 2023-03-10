function solution(dots) {
    const [A, B, C, D] = dots;
    return grad(A, B) === grad(C, D) || grad(A, C) === grad(B, D) || grad(A, D) === grad(B, C) ? 1 : 0;
}

function grad(a, b) {
    return Math.abs((a[1] - b[1]) / (a[0] - b[0]));
}