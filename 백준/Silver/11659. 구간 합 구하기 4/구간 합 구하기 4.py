import sys

n, m = map(int, sys.stdin.readline().split(" "))
arr = list(map(int, sys.stdin.readline().split(" ")))

# O(N) 방식으로 풀 경우,
# O(N*M) = 100,000 * 100,000 = 10,000,000,000 (1초 넘길 수도)

# 누적합 방식
acc = [0] * (n + 1)  # 1-based index
acc[1] = arr[0]

for i in range(2, n + 1):
    acc[i] = arr[i - 1] + acc[i - 1]  # arr은 0-based

for _ in range(m):
    s, e = map(int, sys.stdin.readline().split(" "))
    print(acc[e] - acc[s - 1])
