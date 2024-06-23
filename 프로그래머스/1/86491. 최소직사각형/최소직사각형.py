def solution(sizes):
    for i in range(len(sizes)):
        [w, h] = sizes[i]
        if w < h:
            w, h = h, w
        sizes[i] = [w, h]
    
    max_w = max(w for w, h in sizes)
    max_h = max(h for w, h in sizes)
    
    return max_w * max_h