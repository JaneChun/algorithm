import sys

n, m = map(int, sys.stdin.readline().split(" "))
numbers = sorted(list(map(int, sys.stdin.readline().split(" "))))  # 1, 7, 9, 9
result_set = set()


# dfs로 탐색
def dfs(visited, result):
    if len(result) == m and not tuple(result) in result_set:
        result_set.add(tuple(result))
        print(" ".join(map(str, result)))

    for i in range(n):
        if not visited[i]:
            result.append(numbers[i])
            visited[i] = True
            dfs(visited, result)
            result.pop()
            visited[i] = False


visited = [False] * n
arr = dfs(visited, [])
