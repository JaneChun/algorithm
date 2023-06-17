function solution(genres, plays) {
    const hash = {};
    
    genres
        .map((genre, i) => [genre, plays[i]])
        .forEach(([genre, play], index) => {
        const data = hash[genre] || { total: 0, songs: [] };
        hash[genre] = {
            total: data.total + play, 
            songs: [...data.songs, {play, index}]
                        .sort((a, b) => b.play - a.play)
                        .slice(0, 2)
            }
    })
    
    return Object.entries(hash)
        .sort((a, b) => b[1].total - a[1].total)
        .flatMap((item) => item[1].songs)
        .map((song) => song.index)
}