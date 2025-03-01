def solution(s):
    if len(s) == 1:
        return 1
    
    result = []

    for length in range(1, len(s) // 2 + 1):
        compressed_length = compress(s, length)
        result.append(compressed_length)
    
    return min(result)

def compress(s, n):
    compressed = ''
    count = 1
    prev = s[:n]
    
    for i in range(n, len(s), n):
        cur = s[i:i+n]
        if prev == cur:
            count += 1
        else:
            compressed += (str(count) if count > 1 else '') + prev
            prev = cur
            count = 1
    
    compressed += (str(count) if count > 1 else '') + prev
    
    return len(compressed)
        