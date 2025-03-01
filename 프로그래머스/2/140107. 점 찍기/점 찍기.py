import math

# 시간초과
# def solution(k, d):
#     answer = 0
    
#     for x in range(0, d + 1, k):
#         maxY = math.sqrt(d*d - x*x) # x별로 최고 y 높이 계산

#         for y in range(0, int(maxY) + 1, k):
#             answer += 1

#     return answer

import math

def solution(k, d):
    answer = 0
    
    for x in range(0, d + 1, k):
        maxY = math.sqrt(d*d - x*x) # x별로 최고 y 높이 계산

        answer += (maxY // k) + 1

    return answer