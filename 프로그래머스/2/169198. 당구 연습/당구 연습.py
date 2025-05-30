def solution(m, n, startX, startY, balls):
    answer = []
    
    for x, y in balls:
        min_dist = float('inf')
        
        # 상하좌우 4 방향의 반사점
        top = (x, 2 * n - y)
        bottom = (x, -y)
        left = (-x, y)
        right = (2 * m - x, y)
        
        if not (startX == x and startY < y): # 직선으로 바로 맞출 수 있는 경우는 원쿠션이 아니므로 제외
            distance = get_distance((startX, startY), top)
            min_dist = min(min_dist, distance)
        
        if not (startX == x and startY > y):
            distance = get_distance((startX, startY), bottom)
            min_dist = min(min_dist, distance)
            
        if not (startY == y and startX > x):
            distance = get_distance((startX, startY), left)
            min_dist = min(min_dist, distance)
            
        if not (startY == y and startX < x):
            distance = get_distance((startX, startY), right)
            min_dist = min(min_dist, distance)
            
            
        answer.append(min_dist)
        
    return answer

def get_distance(start, end):
    return (start[0] - end[0]) ** 2 + (start[1] - end[1]) ** 2