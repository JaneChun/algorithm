import sys

n = int(sys.stdin.readline())
meetings = []

for _ in range(n):
    start, end = map(int, sys.stdin.readline().split(" "))
    meetings.append({"start": start, "end": end})

# 끝나는 시간 기준 정렬 -> 시작 시간 기준 정렬
# 빨리 끝나야 그 뒤로 더 많은 회의를 할 수 있으므로
# end가 같으면 일찍 시작한 것부터 담아야 연속으로 넣을 수 있음 e.g. (0, 2) -> (2, 2) -> ...
meetings.sort(key=lambda x: (x["end"], x["start"]))

count = 0
cur = 0
for meeting in meetings:
    start, end = meeting["start"], meeting["end"]
    if cur <= start:
        count += 1
        cur = end

print(count)