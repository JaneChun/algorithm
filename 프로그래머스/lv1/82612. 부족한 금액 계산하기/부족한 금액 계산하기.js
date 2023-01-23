function solution(price, money, count) {
    let cost = 0;

    for (let i = 1; i <= count; i++) {
        cost = cost + price * i;
    }
    
    return cost < money ? 0: cost - money
}