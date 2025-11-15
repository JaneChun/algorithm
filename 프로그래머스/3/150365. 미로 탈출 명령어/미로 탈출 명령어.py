# n x m 격자 미로
# x, y 출발 -> r, c 도착
# 이동하는 거리가 총 k
# 사전 순으로 빠른 경로로 탈출

def solution(n, m, x, y, r, c, k): # 2, 3 -> 3, 1
    answer = ''
    
    dist = abs(x - r) + abs(y - c)
    if k < dist: # k번 안에 못가는 경우
        return 'impossible'
    if (k - dist) % 2 == 1: # 남는 거리가 홀수인 경우(왔다갔다 못함)
        return 'impossible'
    
    direction = {'d': (1, 0), 'l': (0, -1), 'r': (0, 1), 'u': (-1, 0)} # 사전순
    
    # k번 이동
    for step in range(k):
        for di, (dx, dy) in direction.items(): # 상하좌우
            nx, ny = x + dx, y + dy
            n_dist = abs(nx - r) + abs(ny - c)
            n_k = k - (step + 1) # step은 0-based이므로 +1
            
            if 1 <= nx <= n and 1 <= ny <= m and n_k >= n_dist and (n_k - n_dist) % 2 == 0:
                answer += di
                x, y = nx, ny # 현재값 갱신
            
    return answer