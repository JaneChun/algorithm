function solution(today, terms, privacies) {
    const result = [];
    privacies.forEach((privacy, i) => {
        const [dateStr, term] = privacy.split(' ');
        let date = new Date(dateStr);
        const month = terms.find((t) => t[0] === term).split(' ')[1]
        date.setMonth(date.getMonth() + Number(month));
        
        if (new Date(today) >= date) {
            result.push(i + 1);
        }
    })
    
    return result;
}