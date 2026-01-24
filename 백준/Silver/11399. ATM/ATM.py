import sys

n = int(sys.stdin.readline())
p = list(map(int, sys.stdin.readline().split()))

total_time = 0
p.sort()

for i in range(len(p)):
    time = sum(p[: i + 1])
    total_time += time

print(total_time)