function solution(a, b) {
    let days = ['THU', 'FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED'];
    const months = [null, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
    
    let month = 1;
    
    while(month < a) {
        const idx = months[month] % 7;
        days = [...days.slice(idx), ...days.slice(0, idx)];
        month++;
    }
    console.log(month,days)
    return days[b % 7];
}