def solution(line):
    int_intersection = set()
    
    for i in range(len(line) - 1):
        for j in range(i, len(line)):
            result = get_intersection(line[i], line[j])
            
            if result and result[0].is_integer() and result[1].is_integer():
                int_intersection.add((result[0], result[1]))
               
    #  별 찍기
    answer = []
    minY, maxY, minX, maxX = map(int, get_min_max(int_intersection))
    
    for i in range(maxY, minY - 1, -1):
        row = []
        for j in range(minX, maxX + 1):
            if (i,j) in int_intersection:
                row.append('*')
            else:
                row.append('.')
        answer.append(''.join(row))
    
    return answer

def get_intersection(line1, line2):
    A, B, E = line1
    C, D, F = line2
    
    if A*D - B*C == 0:
        return None
    
    x = (B*F - E*D) / (A*D - B*C)
    y = (E*C - A*F) / (A*D - B*C)
    
    return [y, x]

def get_min_max(coords):
    minY, minX = float('inf'), float('inf')
    maxY, maxX = float('-inf'), float('-inf')
    
    for y, x in coords:
        minY = min(y, minY)
        minX = min(x, minX)
        maxY = max(y, maxY)
        maxX = max(x, maxX)
        
    return minY, maxY, minX, maxX