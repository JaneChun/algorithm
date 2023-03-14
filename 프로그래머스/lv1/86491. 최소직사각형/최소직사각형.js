function solution(sizes) {
    let maxWidth = 0, maxHeight = 0;
    sizes.map(([w, h]) => [Math.max(w, h), Math.min(w, h)])
         .forEach(([w, h]) => {
             if (w > maxWidth) maxWidth = w;
             if (h > maxHeight) maxHeight = h;
         })
    return maxWidth * maxHeight;
}