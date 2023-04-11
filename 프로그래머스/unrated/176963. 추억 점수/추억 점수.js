function solution(name, yearning, photo) {
    const hash = {};
    name.forEach((v, i) => hash[v] = yearning[i]);

    return photo.map((item) => item.reduce((acc, person) => hash[person] ? acc + hash[person] : acc, 0));
}