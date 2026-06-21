from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid) # 높이
        n = len(grid[0]) # 너비
        
        # bfs
        visited = [[False] * n for _ in range(m)]
        answer = 0
        
        def bfs(y, x):
            q = deque([(y, x)]) # 시작점
            visited[y][x] = True
            
            while q:
                y, x = q.popleft()

                for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    ny, nx = y + dy, x + dx
                    # 육지이고 방문한 적 없다면 이어서 탐색
                    if 0 <= ny < m and 0 <= nx < n and grid[ny][nx] == '1' and not visited[ny][nx]:
                        q.append((ny, nx))
                        visited[ny][nx] = True
            
            # while 문이 종료되면, y, x를 시작점으로 해서 연결된 모든 땅 탐색 & 방문처리 완료
        
        # 각 칸을 시작점으로 탐색
        for y in range(m):
            for x in range(n):
                if grid[y][x] == '1' and not visited[y][x]:
                    bfs(y, x)
                    answer += 1

        return answer
        