def solution(numbers):
    numbers_set = set()
    
    for i in range(1, len(numbers) + 1):
        perms = permutations(numbers, i)
        numbers_set.update([int(''.join(p)) for p in perms])
        
    return len(list(filter(lambda x: is_prime(x),numbers_set)))
        
def permutations(numbers, length):
    def backtrack(fixed, visited, result):
        
        # 종료 조건
        if len(fixed) == length:
            result.append(fixed[:])
            return
        
        # 요소 순회
        for i in range(len(numbers)):
            # 방문하지 않았다면 방문 처리하고, fixed에 추가하여 다음 단계로 진행
            if not visited[i]:
                fixed.append(numbers[i])
                visited[i] = True
                backtrack(fixed, visited, result)
                
                # 백트레킹
                fixed.pop()
                visited[i] = False
    
    result = []
    visited = [False] * len(numbers)
    
    backtrack([], visited, result)
    
    return result
        
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True