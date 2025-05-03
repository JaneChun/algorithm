def solution(n, q, ans):
    answer = 0
    possible_n = [i for i in range(1, n + 1)]
    
    combis = combinations(possible_n, 5)
    
    for combi in combis:
        if check(combi, q, ans):
            answer += 1
            
    return answer

def combinations(source, count):
    combis = []
    
    def dfs(start, result):
        if len(result) == count:
            combis.append(result[:])
            return
        
        for i in range(start, len(source)):
            result.append(source[i])
            dfs(i + 1, result)
            result.pop()
    
    dfs(0, [])
    
    return combis
    

def check(combi, q, ans):
    for arr, answer in zip(q, ans):
        intersection_count = len(set(combi) & set(arr))
        if intersection_count != answer:
            return False
    
    return True