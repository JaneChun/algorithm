n = int(input())

dp_r = [float('inf')] * n
dp_g = [float('inf')] * n
dp_b = [float('inf')] * n

first_house = list(map(int, input().split(' ')))

dp_r[0] = first_house[0]
dp_g[0] = first_house[1]
dp_b[0] = first_house[2]

for i in range(1, n):
  r, g, b = map(int, input().split(' '))
  if dp_r[i - 1] != float('inf'): # 이전 집이 빨간색이 아니라면, 빨간색을 칠할 수 있다.
    dp_r[i] = r + min(dp_g[i - 1], dp_b[i - 1]) # 이때 dp_r[i] 값은 dp_g[i - 1]와 dp_b[i - 1] 중 작은 값에 현재 빨간색을 칠한 값을 더한 값이다.
  if dp_g[i - 1] != float('inf'):
    dp_g[i] = g + min(dp_r[i - 1], dp_b[i - 1])
  if dp_b[i - 1] != float('inf'):
    dp_b[i] = b + min(dp_r[i - 1], dp_g[i - 1])
    

print(min(dp_r[n - 1], dp_g[n - 1], dp_b[n - 1]))