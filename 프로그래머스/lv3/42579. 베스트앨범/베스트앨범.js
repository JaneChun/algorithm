function solution(genres, plays) {
    const hash = {};
    
    genres.map((genre, i) => [genre, plays[i]])
    // [
    //   [ 'classic', 500 ],
    //   [ 'pop', 600 ],
    //   [ 'classic', 150 ],
    //   [ 'classic', 800 ],
    //   [ 'pop', 2500 ]
    // ]
          .forEach(([genre, play], index) => {
            const data = hash[genre] || { total: 0, songs: [] }; // hash에 저장되어있으면 불러오고, 없으면 {total: 0, songs: []}로 값 추가
            
            hash[genre] = {
                total: data.total + play, // total에 재생수 더하기
                songs: [...data.songs, {play, index}] // songs 배열에 현재 곡을 {play: 500, index: 0}의 형태로 저장하기
                        .sort((a, b) => b.play - a.play) // 재생수 많은 순으로 내림차순 정렬
                        .slice(0, 2) // 베스트 2개만 뽑기
            }
    })
    // console.log(hash)
    // {
    //   classic: { total: 1450, songs: [  { play: 800, index: 3 }, { play: 500, index: 0 } ] },
    //   pop: { total: 3100, songs: [ { play: 2500, index: 4 }, { play: 600, index: 1 } ] }
    // }
    
    // console.log(Object.entries(hash))
    // [
    //   [ 'classic', { total: 1450, songs: [Array] } ],
    //   [ 'pop', { total: 3100, songs: [Array] } ]
    // ]
    
    return Object.entries(hash).sort((a, b) => b[1].total - a[1].total)
                               .flatMap((el) => el[1].songs) // [{ play: 2500, index: 4 }, { play: 600, index: 1 }, { play: 800, index: 3 }, { play: 500, index: 0 }]
                               .map((song) => song.index);
}