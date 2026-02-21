import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split(" "))

graph = {}

for i in range(1, n + 1):
    graph[i] = []

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split(" "))
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n + 1)
q = deque([])


def bfs(start):
    q.append(start)
    visited[start] = True

    while q:
        cur = q.popleft()

        for next in graph[cur]:
            if not visited[next]:
                q.append(next)
                visited[next] = True


count = 0
for i in range(1, n + 1):
    if not visited[i]:
        bfs(i)  # 새로운 덩어리 탐색 시작
        count += 1

print(count)