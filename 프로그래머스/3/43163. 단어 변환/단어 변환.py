def solution(begin, target, words):
    queue = [(begin, 0)]
    visited = [False] * len(words)
    
    while queue:
        cur, cnt = queue.pop(0)
        if cur == target:
            return cnt
        
        for i in range(len(words)):
            if one_letter_different(cur, words[i]) and not visited[i]:
                queue.append((words[i], cnt + 1))
                visited[i] = True
                
    return 0
        
def one_letter_different(a, b):
    count = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            count += 1
            
    return count == 1