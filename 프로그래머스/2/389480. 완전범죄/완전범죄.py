def solution(info, n, m):
    answer = 121
    visited = [[[False for _ in range(m)] for _ in range(n)] for _ in range(len(info) + 1)] 
    # [index][a][b] = False

    
    def dfs(index, a, b):
        nonlocal answer
        
        if a >= n or b >= m:
            return
        
        if visited[index][a][b]:
            return
        
        if index == len(info):
            answer = min(answer, a)
            return

        visited[index][a][b] = True
        
        # a가 훔치는 경우
        dfs(index + 1, a + info[index][0], b)
        
        # b가 훔치는 경우
        dfs(index + 1, a, b + info[index][1])
        
    dfs(0, 0, 0)
    
    return answer if answer != 121 else -1


# info의 길이가 최대 40이기 때문에 DFS만으로는 최대 2^40 (약 1조) 가지 분기를 탐색 -> 방문 여부 메모이제이션