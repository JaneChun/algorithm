function solution(n, costs) {
    let totalCost = 0;
    let bridgeCount = 0;
    costs.sort((a, b) => a[2] - b[2]);
    const parent = makeParent(n);
    
    for (const [a, b, cost] of costs) {
        if (bridgeCount === n) break;
        
        if (findParent(parent, a, b)) {
            continue;
        } else {
            totalCost += cost;
            bridgeCount++;
            unionParent(parent, a, b);
        }
    }
    
    return totalCost;
}

const makeParent = (n) => {
    return Array.from(Array(n), (_, i) => i++);
}

const getParent = (parent, x) => {
    if (parent[x] === x) return x;
    return getParent(parent, parent[x]);
}

const unionParent = (parent, x, y) => {
    const n1 = getParent(parent, x);
    const n2 = getParent(parent, y);
    if (n1 < n2) return parent[n2] = n1;
    else return parent[n1] = n2;
}

const findParent = (parent, x, y) => {
    const n1 = getParent(parent, x);
    const n2 = getParent(parent, y);
    if (n1 === n2) return true;
    else return false;
}

