def solution(places):
    answer = []
    for place in places:
        if is_all_distanced(place):
            answer.append(1)
        else:
            answer.append(0)
    return answer

def is_all_distanced(place):
    for row in range(len(place)):
        for col in range(len(place[row])):
            if place[row][col] == 'P':
                # 맨해튼 거리두기를 지고 있는지 확인
                if is_someone_around(place, [row, col]):
                    return False
    return True

# bfs로 확인
def is_someone_around(place, start):
    queue = []
    visited = [[False for j in range(5)] for i in range(5)]
    
    queue.append([start, 0]) # [y, x], 누적거리
    visited[start[0]][start[1]] = True
    
    while queue:
        (y, x), dis = queue.pop(0)
        
        if 1 <= dis <= 2 and place[y][x] == 'P':
            return True
        
        for dy, dx in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            ny = y + dy
            nx = x + dx
            if (0 <= ny < 5 and 
                0 <= nx < 5 and 
                not visited[ny][nx] and 
                place[ny][nx] != 'X' and 
                dis < 2
               ):
                queue.append([[ny, nx], dis + 1])
                visited[ny][nx] = True
    return False