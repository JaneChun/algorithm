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

// solution("2022.05.19", ["A 6", "B 12", "C 3"], ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"])