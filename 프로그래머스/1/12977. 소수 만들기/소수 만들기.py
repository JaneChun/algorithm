def solution(nums):
    def isPrimeNumber(num):
        if num <= 1 or num % 2 == 0:
            return False
        elif num == 2:
            return True
        else:
            for i in range(3, int(num ** 0.5) + 1, 2):
                if num % i == 0:
                    return False
            return True
    
    results = []
    visited = [False] * len(nums)
    
    def dfs(sum, depth, start_idx):
        if depth == 3:
            if isPrimeNumber(sum):
                results.append(sum)
            return
        
        for i in range(start_idx, len(nums)):
            if not visited[i]:
                visited[i] = True
                dfs(sum + nums[i], depth + 1, i + 1)
                visited[i] = False
        
    
    dfs(0, 0, 0)
    
    return len(results)