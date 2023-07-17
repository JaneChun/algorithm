function solution(tickets) {
    const used = Array(tickets.length).fill(false);
    const route = [];
    let count = 0;
    
    tickets.sort((a, b) => a[0] !== b[0] ? a[0].localeCompare(b[0]) : a[1].localeCompare(b[1]));
    
    const dfs = (departure, route, count) => {
        if (count === tickets.length) {
            route.push(departure)
            return true;
        }
        
        for (let i = 0; i < tickets.length; i++) {
            const [from, to] = tickets[i];
            if (departure === from && !used[i]) {
                route.push(departure);
                used[i] = true;
                if(dfs(to, route, count + 1)) return true;
                used[i] = false;
            }
        }
        
        route.pop();
        return false;
    }
    
    dfs('ICN', route, count);

    return route;
}