import sys

n, m = map(int, sys.stdin.readline().split(" "))
trees = list(map(int, sys.stdin.readline().split(" ")))

left = 0
right = max(trees)
mid = (left + right) // 2

while left <= right:
    mid = (left + right) // 2
    woods = list(map(lambda x: max(0, x - mid), trees))
    sum_woods = sum(woods)

    if sum_woods < m:  # 나무가 부족 -> 절단기의 높이를 낮춰야 함
        right = mid - 1
    else:
        left = mid + 1  # 나무가 충분 -> 절단기의 높이를 높여야 함

print(right)