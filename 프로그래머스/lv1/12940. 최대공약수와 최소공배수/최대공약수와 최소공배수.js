function solution(n, m) {
    const nm = n*m
  	for (let r; r = n % m; n = m, m = r) {
    }
  	return [m, nm/m];
}