n = int(input())

meetings = []
for i in range(n):
    a, b = map(int, input().split())
    meetings.append((a, b))

sort_meetings = sorted(meetings, key=lambda x: (x[1], x[0]))

count = 0
time = 0
for s, e in sort_meetings:
  if time <= s:
    count += 1
    time = e

print(count)