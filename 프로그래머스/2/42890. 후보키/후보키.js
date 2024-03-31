// 조합 생성 함수
function makeCombinations (arr, level) { // [1,2,3], 2
    if (level === 1) return arr.map((v) => [v])// [2] [3]
    
    const result = []
    arr.forEach((fixed, i, origin) => { // fixed = 1, rest = [2, 3]
        const rest = origin.slice(i + 1) // fixed를 제외한 나머지에 대해서 조합을 구한다.
        const combinations = makeCombinations(rest, level - 1) // [2] [3]

        const attached = combinations.map(v => [fixed, ...v]) // 돌아온 조합에 떼놓은 값(fixed)를 붙인다.
        result.push(...attached) // [1,2], [1,3], [2,3]
    });
    return result
}

// 유일성 체크 함수
function checkUniqueness(arr) {
    const set = new Set()
    for (const item of arr) {
        if (set.has(item)) return false // 중복이 발생하면 유일성을 만족하지 않음
        set.add(item)
    }
    return true // 중복이 없으면 유일성을 만족함
}

// 최소성 체크 함수
function checkMinimality(idxArray, candidates) { // [[0]] 후보키 배열을 순회하며
    for (const candidate of candidates) { // [0] 후보키 배열의 모든 요소가 입력된 idxArray에 포함되는지 확인
        for (let i = 0; i < candidate.length; i++) { // [0]
            if (candidate.every(key => idxArray.includes(key))) { // 최소성 만족 X
                return false
            }
        }
    }
    return true // 최소성 만족
}

function solution(relation) {
    let count = 0
    
    const columnIdxArray = Array.from({length: relation[0].length}, (_, i) => i) // [ 0, 1, 2, 3 ]
    const columnIdxCombinations = columnIdxArray.reduce((acc, _, i) => {
        acc.push(...makeCombinations(columnIdxArray, i + 1))
        return acc
    }, [])
    console.log(columnIdxCombinations)
    // [
    //   [ 0 ], [ 1 ], [ 2 ], [ 3 ],
    //   [ 0, 1 ], [ 0, 2 ], [ 0, 3 ], [ 1, 2 ], [ 1, 3 ], [ 2, 3 ],
    //   [ 0, 1, 2 ], [ 0, 1, 3 ], [ 0, 2, 3 ], [ 1, 2, 3 ],
    //   [ 0, 1, 2, 3 ]
    // ]
    
    const candidates = [] // 후보키
    
    columnIdxCombinations.forEach((idxArray) => { // [0, 1]
        const arr = relation.map((row) => idxArray.map((idx) => row[idx]).join(''))
        console.log('arr', arr)
        if (checkUniqueness(arr) && checkMinimality(idxArray, candidates)) {
            candidates.push(idxArray)
        }
    })
    
    return candidates.length
}