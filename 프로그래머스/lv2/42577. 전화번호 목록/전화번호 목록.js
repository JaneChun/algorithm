function solution(phone_book) {
    const hash = {};
    phone_book.forEach((v) => hash[v] = true);
    
    for (const number of phone_book) {
        for (let i = 0; i < number.length; i++) {
            const sliced = number.slice(0, i + 1)
            hash[number] = false;
            if (hash[sliced]) return false;
            hash[number] = true;
        }
    }
    return true;
}