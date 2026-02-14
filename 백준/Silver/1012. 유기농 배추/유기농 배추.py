import sys
# python의 재귀 제한은 1000인데 이 문제에서 배추의 최대 개수는 2500개로, 모두 연결되어 있다면 재귀 깊이가 2500 까지 갈 수 있음 -> RecursionError
sys.setrecursionlimit(10000)

T = int(sys.stdin.readline())

for _ in range(T):
    M, N, K = map(int, sys.stdin.readline().split(" "))
    graph = [[0 for _ in range(M)] for _ in range(N)]

    # graph 생성
    for _ in range(K):
        x, y = map(int, sys.stdin.readline().split(" "))
        graph[y][x] = 1

    # dfs 탐색
    visited = [[False for _ in range(M)] for _ in range(N)]
    count = 0

    def dfs(y, x):
        for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            ny, nx = y + dy, x + dx

            # 다음 탐색지가 범위 내이고, 배추가 있고, 방문한 적 없다면 이어서 깊이 탐색
            if (
                0 <= ny < N
                and 0 <= nx < M
                and graph[ny][nx] == 1
                and not visited[ny][nx]
            ):
                visited[ny][nx] = True
                dfs(ny, nx)

            # 더이상 탐색할 곳이 없다면 함수가 종료됨

    for y in range(N):
        for x in range(M):
            # 새로운 군집 탐색 시작
            if graph[y][x] == 1 and not visited[y][x]:
                visited[y][x] = True
                count += 1
                dfs(y, x)

    print(count)
