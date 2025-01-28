# 아무 회전도 하지 않았을 때, i 행 j 열에 있는 숫자는 ((i-1) x columns + j
def solution(rows, columns, queries):
    answer = []
    matrix = [[(i * columns) + (j + 1) for j in range(columns)] for i in range(rows)]
    
    for query in queries:
        y1, x1, y2, x2 = [q - 1 for q in query] # 0 based index로 변환
        temp = matrix[y1][x1] # 시작값 보관
        min_value = temp # 최소값
        
        # ⬇️
        for i in range(y1, y2):
            matrix[i][x1] = matrix[i + 1][x1]
            min_value = min(min_value, matrix[i][x1])

        # ➡️
        for j in range(x1, x2):
            matrix[y2][j] = matrix[y2][j + 1]
            min_value = min(min_value, matrix[y2][j])
        
        # ⬆️
        for i in range(y2, y1, -1):
            matrix[i][x2] = matrix[i - 1][x2]
            min_value = min(min_value, matrix[i][x2])
        
        # ⬅️
        for j in range(x2, x1, -1):
            matrix[y1][j] = matrix[y1][j - 1]
            min_value = min(min_value, matrix[y1][j])
        
        matrix[y1][x1 + 1] = temp
        answer.append(min_value)
    return answer