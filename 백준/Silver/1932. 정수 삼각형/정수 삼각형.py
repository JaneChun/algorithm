# 각 층을 내려가면 합 누적하고 마지막 열 5개중에 가장 큰 값 출력하기
import sys
import copy

n = int(sys.stdin.readline())
triangle = []

for _ in range(n):
  arr = list(map(int, sys.stdin.readline().split(' ')))
  triangle.append(arr)
  
# [[7],            -> [0][0]
# [3, 8],          -> [1][0] [1][1]
# [8, 1, 0],       -> [2][0] [2][1] [2][2]
# [2, 7, 4, 4],    -> [3][0] [3][1] [3][2] [3][3] 
# [4, 5, 2, 6, 5]] -> [4][0] [4][1] [4][2] [4][3] [3][4]

# [0][0] => [1][0], [1][1] 에 더하기
# [1][0] => [2][0], [2][1] 에 더하기
# [1][1] => [2][1], [2][2] 에 더하기
# 규칙: [i][j] => [i+1][j], [1+1][j+1]에 더하기 ([2][1]처럼 한 자리에 겹치기 때문에, 최대값을 갱신)

result = copy.deepcopy(triangle)
for i in range(n - 1):
  for j in range(len(triangle[i])):
    cur = result[i][j]
    result[i+1][j] = max(result[i+1][j], triangle[i+1][j] + cur)
    result[i+1][j+1] = max(result[i+1][j+1], triangle[i+1][j+1] + cur)

print(max(result[n - 1]))