# 매분마다 썩은 오렌지와 상하좌우로 인접한 오렌지도 썩음
# 모든 오렌지가 썩을 때까지 걸리는 최소 시간을 구하고
# 불가능한 경우 -1을 리턴하라

from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        # 썩은 오렌지를 모두 구하고,
        # 모든 썩은 오렌지를 시작점으로 bfs 탐색을 한다.        

        # 멀티 소스 bfs
        q = deque()
        visited = [[-1] * n for _ in range(m)]

        for y in range(m):
            for x in range(n):
                if grid[y][x] == 2:
                    q.append((y, x, 0)) # y, x, time
                    visited[y][x] = 0

        while q:
            y, x, t = q.popleft()
            
            for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                ny, nx = y + dy, x + dx
                if 0 <= ny < m and 0 <= nx < n and grid[ny][nx] == 1 and visited[ny][nx] == -1:
                    q.append((ny, nx, t + 1))
                    visited[ny][nx] = t + 1
            
        last_time = 0
        for y in range(m):
            for x in range(n):
                if grid[y][x] == 1 and visited[y][x] == -1: # 안썩은 오렌지가 하나라도 있다면 -1 리턴
                    return -1
                last_time = max(last_time, visited[y][x])
        return last_time
            