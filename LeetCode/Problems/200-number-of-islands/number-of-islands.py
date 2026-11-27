from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def bfs(start):
            y, x = start
            q = deque([(y, x)])
            grid[y][x] = "0" # 방문 처리
            
            direction = [(-1,0), (1,0), (0,-1), (0,1)]

            while q:
                y, x = q.popleft()

                for dy, dx in direction:
                    ny, nx = y + dy, x + dx

                    if 0 <= ny < n and 0 <= nx < m and grid[ny][nx] == "1":
                        q.append((ny, nx))
                        grid[ny][nx] = "0" 
                        # 큐에 넣을 때 방문 처리하는 이유: 
                        # 큐에서 꺼낼 때 방문 처리를 하면 큐에 있는 동안 다른 이웃으로 인해 방문되어도 또 같은 칸이 큐에 들어감
                        # 중복이 쌓이면서 메모리 초과

        m = len(grid[0])
        n = len(grid)
        count = 0
    
        for y in range(n):
            for x in range(m):
                if grid[y][x] == "1":
                    bfs((y, x))
                    count += 1
        
        return count
        