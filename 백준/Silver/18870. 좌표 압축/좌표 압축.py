import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split(" ")))

# 중복 제거 후 정렬
sorted_arr = sorted(set(arr))
sorted_map = {value: i for i, value in enumerate(sorted_arr)}

result = [sorted_map[value] for value in arr]
print(" ".join(map(str, result)))
