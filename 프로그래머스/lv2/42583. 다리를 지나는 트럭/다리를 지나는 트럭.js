function solution(bridge_length, weight, truck_weights) {
    let time = 0;
    const bridge = new Array(bridge_length).fill(0);
    let currentBridgeWeight = 0;
    
    
    while (truck_weights.length) {
        // dequeue
        bridge.shift();
        // enqueue
        currentBridgeWeight = bridge.reduce((acc, cur) => acc + cur, 0)
        if (currentBridgeWeight + truck_weights[0] <= weight) { // 1. 다리 무게 초과 안하면 넣고
            const shifted = truck_weights.shift()
            bridge.push(shifted);
            currentBridgeWeight += shifted;
        } else { // 2. 초과하면 안넣음
            bridge.push(0);
        }
        
        time++;
    }
    
    return time + bridge_length;
}