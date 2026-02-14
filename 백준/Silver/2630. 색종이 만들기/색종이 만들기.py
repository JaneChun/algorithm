import sys

n = int(sys.stdin.readline())
board = []
white = 0
blue = 0

for _ in range(n):
    row = list(map(int, sys.stdin.readline().split(" ")))
    board.append(row)


def partition(x, y, size):
    global white, blue

    color = board[y][x]  # 첫번째 칸의 색
    is_same = True  # 모든 칸이 같은 색인지 플래그

    for i in range(y, y + size):
        for j in range(x, x + size):
            if board[i][j] != color:
                is_same = False
                break
        if not is_same:
            break

    # 모든 칸의 색이 같은 경우
    if is_same:
        if color == 0:
            white += 1
        else:
            blue += 1
        return

    # 색이 다른 경우 -> 4등분 하여 재귀
    half = size // 2  # 절반 자르기
    partition(x, y, half)
    partition(x + half, y, half)
    partition(x, y + half, half)
    partition(x + half, y + half, half)


partition(0, 0, n)

print(white)
print(blue)
