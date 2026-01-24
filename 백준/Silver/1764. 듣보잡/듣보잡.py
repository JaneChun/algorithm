import sys

n, m = map(int, sys.stdin.readline().split())

not_heard = set()
not_seen = set()

for _ in range(n):
    name = sys.stdin.readline().strip()
    not_heard.add(name)

for _ in range(m):
    name = sys.stdin.readline().strip()
    not_seen.add(name)

not_heard_seen = not_heard & not_seen

print(len(not_heard_seen))

for name in sorted(not_heard_seen):
    print(name)
