# 시간초과
# def solution(n, left, right):
#     answer = []
    
#     for i in range(1, n + 1):
#         for j in range(1, n + 1):
#             if j <= i:
#                 answer.append(i)
#             else:
#                 answer.append(j)
    
#     return answer[left:right + 1]

def solution(n, left, right):
    answer = []
    for i in range(left, right + 1):
        row = i // n # 해당 인덱스가 몇 번째 행에 있는지
        col = i % n # 해당 인덱스가 그 행에서 몇 번째 열에 있는지
        answer.append(max(row, col) + 1)
    return answer

# 0 1 2 (0, 0) (0, 1) (0, 2)
# 3 4 5 (1, 0) (1, 1) (1, 2)
# 6 7 8 (2, 0) (2, 1) (2, 2)

# 1 2 3
# 2 2 3 
# 3 3 3