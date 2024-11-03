# def solution(land):
#     answer = 0
#     last_col = 0
    
#     for row in land:
#         max_score = 0
        
#         for i in range(len(row)):
#             cur = row[i]
#             if cur > max_score and i != last_col:
#                 max_score = cur
            
#         answer += max_score
#         last_col = row.index(max_score)
#         print(max_score)

#     return answer

def solution(land):
    for i in range(len(land) - 1):
        cur_row = land[i]
        max_score = max(cur_row)
        max_index = cur_row.index(max_score)
        second_max_score = -1
        
        for j in range(len(cur_row)):
            if j != max_index and cur_row[j] > second_max_score:
                second_max_score = cur_row[j]
        
        next_row = land[i + 1]
        for j in range(len(next_row)):
            if j == max_index:
                next_row[j] += second_max_score
            else:
                next_row[j] += max_score
   
    return max(land[-1])